import lexer as lex
from collections import deque
import logging

logger = logging.getLogger(__name__)

# Simulates a token stream that allows unreading the tokens
# to some preset length (default is 2, i.e. two tokens can be unread/pushed back)
# None : signifies the end of token stream
class Lexer:
    def __init__(self, inptline, maxhistory=2):

        self.tokgen = lex.tokenize(inptline)

        self.maxhistory = maxhistory
        self.tokqueue = deque(maxlen=self.maxhistory)
        self.tokindex = 0
        self.tokstreamended = False
        self.currtok = None  # the current token returned

        # read all the tokens untill the queue is full
        # or the tokens are finished, which ever is first.
        count = 0
        while count < self.maxhistory:
            if self.tokstreamended:
                self.tokqueue.append(None)
                count += 1
                continue

            try:
                tok = next(self.tokgen)
                self.tokqueue.append(tok)

            except:
                # signifies that the self.tokgen has run out of tokens
                # None signifies that the token stream ends.
                self.tokqueue.append(None)
                self.tokstreamended = True
            count += 1
        logger.info(self.tokqueue)

        self.tokstreamended = False # for nextok() to use it fresh

    def nextToken(self):
        """
        Returns the next token or None if the stream has ended.
        When the stream has ended, the last element of the buffer is None.
        """
        tok = None

        if self.tokindex < self.maxhistory:
            tok = self.tokqueue[self.tokindex]
            logger.debug("self.tokindex = %s", self.tokindex)
            self.tokindex += 1
        else:
            if self.tokstreamended: return None
            try:
                tok = next(self.tokgen)
                self.tokqueue.append(tok)
            except:
                # signifies that the self.tokgen has run out of tokens
                # None signifies that the token stream has ended.
                tok = None  # necessary
                self.tokqueue.append(None)
                self.tokstreamended = True

        self.currtok = tok
        return tok

    def prevToken(self):
        """
        Shifts the internal index to the previous token returned.
        Returns True if there is a previous token left.
        """
        if self.tokindex > 0:
            self.tokindex -= 1
            return True
        return False

    def token(self):
        """
        Returns the last token fetchech using nexttok()
        """
        return self.currtok


