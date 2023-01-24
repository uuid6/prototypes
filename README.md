# Prototypes
Draft Prototypes and Tests for UUIDv6 and beyond

| Name                                                                                             | Language   | UUIDv6 | UUIDv7 | UUIDv8 | RFC/Draft |
|--------------------------------------------------------------------------------------------------|------------|--------|--------|--------|-----------|
| [uuid6/prototypes/python](https://github.com/uuid6/prototypes/tree/main/python)                  | Python     | Yes    | Yes    | Yes    | [02][02]  |
| [oittaa/uuid6-python](https://github.com/oittaa/uuid6-python)                                    | Python     | Yes    | Yes    | No     | [04][04]  |
| [jdknezek/uuid6-zig](https://github.com/jdknezek/uuid6-zig)                                      | Zig        | Yes    | Yes    | No     | [03][03]  |
| [daegalus/uuid/tree/uuid6](https://github.com/Daegalus/dart-uuid/tree/uuidv6)                    | Dart       | Yes    | Yes    | Yes    | [04][04]  |
| [f4b6a3/uuid-creator](https://github.com/f4b6a3/uuid-creator)                                    | Java       | Yes    | Yes    | No     | [04][04]  |
| [chrylis/time-based-uuid-reordering](https://github.com/chrylis/time-based-uuid-reordering)      | Java       | Yes    | No     | No     | [04][04]  |
| [mikemix/php-uuid-v6](https://github.com/mikemix/php-uuid-v6)                                    | PHP        | Yes    | No     | No     | [0x][0x]  |
| [oittaa/uuid-php](https://github.com/oittaa/uuid-php)                                            | PHP        | Yes    | Yes    | No     | [04][04]  |
| [symfony/uid](https://github.com/symfony/uid/tree/6.2)                                           | PHP        | Yes    | Yes    | Yes    | [04][04]  |
| [kurttheviking/uuid-with-v6-js](https://github.com/kurttheviking/uuid-with-v6-js)                | JavaScript | Yes    | No     | No     | [0x][0x]  |
| [bradleypeabody/gouuidv6](https://github.com/bradleypeabody/gouuidv6)                            | Go         | Yes    | No     | No     | [0x][0x]  |
| [gofrs/uuid](https://github.com/gofrs/uuid)                                                      | Go         | Yes    | Yes    | No     | [0x][0x]  |
| [sprql/uuid7-ruby](https://github.com/sprql/uuid7-ruby)                                          | Ruby       | No     | Yes    | No     | [01][01]  |
| [kjmph/UUID_v7_for_Postgres.sql](https://gist.github.com/kjmph/5bd772b2c2df145aa645b837da7eca74) | Postgres   | No     | Yes    | Yes    | [03][03]  |
| [MatrixAI/js-id](https://github.com/MatrixAI/js-id)                                              | TypeScript | No     | Yes    | No     | [01][01]  |
| [LiosK/uuidv7](https://github.com/LiosK/uuidv7)                                                  | TypeScript | No     | Yes    | No     | [04][04]  |
| [kripod/uuidv7](https://github.com/kripod/uuidv7)                                                | TypeScript | No     | Yes    | No     | [04][04]  |
| [karwa/uniqueid](https://github.com/karwa/uniqueid)                                              | Swift      | Yes    | No     | No     | [02][02]  |
| [fabiolimace/UUIDv7_for_C](https://gist.github.com/fabiolimace/9873fe7bbcb1e6dc40638a4f98676d72) | C          | No     | Yes    | No     | [03][03]  |
| [LiosK/uuidv7-h](https://github.com/LiosK/uuidv7-h)                                              | C/C++      | No     | Yes    | No     | [04][04]  |
| [mareek/UUIDNext](https://github.com/mareek/UUIDNext)                                            | C#         | Yes    | Yes    | Yes     | [04][04]  |
| [BaerMitUmlaut/GuidPlus](https://github.com/BaerMitUmlaut/GuidPlus)                              | C#         | Yes    | Yes    | Yes    | [02][02]  |
| [LiosK/uuid7-rs](https://github.com/LiosK/uuid7-rs)                                              | Rust       | No     | Yes    | No     | [04][04]  |
| [DianaNites/nuuid](https://github.com/DianaNites/nuuid)                                          | Rust       | Yes    | Yes    | Yes    | [04][04]  |
| [jakwings/uuid.sh](https://github.com/jakwings/uuid.sh)                                          | Shell      | Yes    | Yes    | Yes    | [04][04]  |

*Note: UUIDv8 prototypes will likely vary among implementations*

# Contributing
Create a repository and open a Pull Request to have this table updated.

Please include:
- Link to repository
- Programming language used
- List UUIDvX versions supported in repository
- Define RFC version you are implementing (Preferably the [latest available](https://datatracker.ietf.org/doc/draft-peabody-dispatch-new-uuid-format/))
- Any comments/notes to include

[0x]: http://gh.peabody.io/uuidv6/
[01]: https://tools.ietf.org/html/draft-peabody-dispatch-new-uuid-format-01
[02]: https://tools.ietf.org/html/draft-peabody-dispatch-new-uuid-format-02
[03]: https://tools.ietf.org/html/draft-peabody-dispatch-new-uuid-format-03
[04]: https://tools.ietf.org/html/draft-peabody-dispatch-new-uuid-format-04
