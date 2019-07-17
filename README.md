# python-semi-advanced

## Git Cheatsheet

W tabeli poniżej znajdują się polecenia, których używaliśmy na zajęciach. Ciekawa ściągawka dostępna jest pod [tym](https://www.git-tower.com/blog/git-cheat-sheet/?utm_source=hashnode.com) linkiem.

|       Polecenie                           |      Skutek                                                                                 |
| :---------------------------------------- | :------------------------------------------------------------------------------------------ |
| git config --global user.name "username"  | ustawia login użytkownika                                                                   |
| git config --global user.email "email"    | ustawia email użytkownika                                                                   |
| git config user.email                     | wyświetla email użytkownika                                                                 |
| git config user.user                      | wyświetla login użytkownika                                                                 |
| git init                                  | tworzy nowe repozytorium                                                                    |
| git checkout <hash commit>                | repo przechodzi na dany commit                                                              |
| git checkout HEAD^^                       | repo przechodzi na dwa commity wcześniej                                                    |
| git checkout HEAD~2                       | repo przechodzi na dwa commity wcześniej                                                    |
| git checkout @^^                          | repo przechodzi na dwa commity wcześniej                                                    |
| git checkout <nazwa brancha>              | repo przechodzi na dany branch                                                              |
| git checkout <nazwa taga>                 | repo przechodzi na dany tag                                                                 |
| git clone <link>                          | kopiuje repozytorium ze zdalnego serwera                                                    |
| git branch                                | pokazuje wszystkie branche; aktualny z gwiazdką                                             |
| git branch -a                             | pokazuje wszystkie branche, również remote; aktualny z gwiazdką                             |
| git branch <nazwa>                        | tworzy nowy branch, ale na niego nie przechodzi                                             |
| git checkout -bwa>                        | tworzy nowy branch, i na niego przechodzi                                                   |
| git commit                                | otwiera edytor w celu podania commit message                                                |
| git commit -m "commit message"            | tworzy commit z wiadomością "commit message"                                                |
| git push                                  | wypycha commity z lokalnego repo na serwer                                                  |
| git merge <nazwa brancha>                 | wrzuca zmiany z podanego brancha na aktualny branch                                         |
| git log                                   | pokazuje historię bieżącej gałęzi                                                           |
| git log --oneline                         | j.w. ale każdy commit w jednej linijce                                                      |
| git status                                | pokazuje pliki, które się zmieniły, pojawiły lub zostały dodane do repo po ostatnim commicie|

## Linux Cheatsheet

|       Polecenie                 |      Skutek                                                                                 |
| :------------------------------ | :------------------------------------------------------------------------------------------ |
| cd scieżka_do_katalogu          | Zmienia katalog do wskazanego jeżeli istnieje                                               |
| mkdir nazwa                     | Utworz katalog o podanej nazwie                                                             |
| mkdir -p nazwa1/nazwa2/nazwa3   | Utwórz zagnieżdżone katalogi                                                                |
| ls                              | Wydrukuj pliki i katalogi znajdujące się w obecnym katalogu                                 |
| ls -a                           | Wydrukuj pliki i katalogi znajdujące się w obecnym katalogu w tym ukryte                    |
| touch nazwa                     | Utwórz nowy plik                                                                            |
| cat plik.txt                    | Wydrukuj plik tekstowy                                                                      |
| less plik.txt                   | Wyświetla iteraktywnie; przewija się enterem                                                |
| echo <cokolwiek>                | Drukuje <cokolwiek> na ekran                                                                |
| <cokolwiek> > plik.txt          | Wrzuca wynik działania <cokolwiek> do plik.txt                                              |
| <cokolwiek> >> plik.txt         | Wrzuca wynik działania <cokolwiek> na koniec plik.txt (dopisuje)                            |

