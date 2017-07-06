The C Language Grammar
=========================

    translation_unit    : external_declaration
                        | translation_unit external_declaration

    external_declaration    : function_definition
                            | declaration

    function_declaration    : declarator compund_statement
                            | declarator declaration_list compound_statement
                            | declaration_specifiers declarator compound_statement
                            | declaration_specifiers declarator declaration_list compound_statement

    declaration : declaration_specifiers
                | init_declaration_list ;

    declaration_list    : declaration
                        | declaration_list declaration

    declaration_specifiers  : storage_class_specifier
                            | storage_class_specifier declaration_specifiers
                            | type_specifier
                            | type_specifier declaration_specifiers
                            | type_qualifier
                            | type_qualifier declaration_specifiers

    storage_class_specifier : AUTO
                            | REGISTER
                            | STATIC
                            | EXTERN
                            | TYPEDEF

    type_specifier  : VOID
                    | CHAR
                    | SHORT
                    | INT
                    | LONG
                    | FLOAT
                    | DOUBLE
                    | SIGNED
                    | UNSIGNED
                    | struct_or_union_specifier
                    | enum_specifier
                    | IDENTIFIER

    type_qualifier  : CONST
                    | VOLATILE


