import pytest
import random
from src.Library import Book, Magazine, Library, BookCollection, IndexDict, Item
from src.Casino import Player, Goose, Casino, GooseCollection, PlayerCollection, ChipBalanceDict


def test_book_init():
    book = Book("Book1", "Author1", 2000, "Genre1", "12345")

    assert book.title == "Book1"
    assert book.author == "Author1"
    assert book.year == 2000
    assert book.genre == "Genre1"
    assert book.isbn == "12345"
    assert book.in_library == True


def test_magazine_init():
    magazine = Magazine("Magazine1", 2000, "Theme1", "67890")


    assert magazine.title == "Magazine1"
    assert magazine.year == 2000
    assert magazine.theme == "Theme1"
    assert magazine.isbn == "67890"
    assert magazine.in_library == True


def test_player_init():
    player = Player("Player1")

    assert player.name == "Player1"
    assert player.chips == 20
    assert player.is_alive == True




def test_goose_init():
    goose = Goose("Goose1")

    assert goose.name == "Goose1"
    assert goose.stolen_chips == 0
    assert goose.is_alive == True


def test_item_take():
    book = Book("Test Book", "Author", 2020, "Genre", "111")
    res = book.take_item()


    assert res == 0
    assert book.in_library == False




def test_item_return():
    book = Book("Test Book", "Author", 2020, "Genre", "222")
    book.take_item()

    res = book.return_item()


    assert res == 1
    assert book.in_library == True


def test_item_take2():
    book = Book("Test Book", "Author", 2020, "Genre", "333")
    book.take_item()

    res = book.take_item()



    assert res == 1






def test_item_return2():
    book = Book("Test Book", "Author", 2020, "Genre", "444")
    res = book.return_item()

    assert res == 0


def test_player_bet2():
    player = Player("Player")
    player.chips = 0
    res = player.bet()
    assert res == 0


def test_player_panic():
    player = Player("Player")

    in_chips = player.chips

    lost = player.panic()


    assert lost > 0
    assert player.chips < in_chips



def test_goose_steal():
    player = Player("Player")
    goose = Goose("Goose")
    in_pl_ch = player.chips
    in_go_st = goose.stolen_chips
    stolen = goose.steal_chips(player)
    

    assert stolen >= 0
    assert player.chips < in_pl_ch

    assert goose.stolen_chips > in_go_st


def test_goose_steal2():
    player = Player("Player")
    player.chips = 0
    goose = Goose("Goose")
    stolen = goose.steal_chips(player)
    assert stolen == 0


def test_library_add():
    library = Library()

    book = Book("Book", "Author", 2000, "Genre", "555")
    res = library.add_book(book)
    assert res == 0


    assert len(library.books) == 1




def test_library_remove():
    library = Library()
    book = Book("Book", "Author", 2000, "Genre", "666")
    library.add_book(book)

    res = library.remove_book(book)
    assert res == 0

    assert len(library.books) == 0


def test_library_remove2():
    library = Library()

    book = Book("Book", "Author", 2000, "Genre", "777")
    res = library.remove_book(book)
    assert res == 1



def test_library_search():
    library = Library()

    book = Book("Book", "Author", 2000, "Genre", "888")
    library.add_book(book)

    fn = library.search_isbn("888")


    assert fn is not None
    assert fn.title == "Book"


def test_library_search2():
    library = Library()



    book = Book("Book", "Author", 2000, "Genre", "999")
    library.add_book(book)
    
    fn = library.search_isbn("000")
    assert fn is None

def test_library_search3():
    library = Library()
    book1 = Book("Book1", "Author", 2000, "Genre", "101")
    book2 = Book("Book2", "Author", 2001, "Genre", "102")

    book3 = Book("Book3", "Other", 2000, "Genre", "103")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    res = library.search_author("Author")
    
    assert len(res) == 2
    assert book1 in res

    assert book2 in res
    assert book3 not in res


def test_library_search4():
    library = Library()
    book = Book("Book", "Author", 2000, "Genre", "104")
    library.add_book(book)
    res = library.search_author("AAA")
    assert len(res) == 0

def test_library_search5():
    library = Library()
    book = Book("Book", "Author", 2020, "Genre", "105")
    magazine = Magazine("Magazine", 2020, "Theme", "106")
    library.add_book(book)
    library.add_book(magazine)

    
    res = library.search_year(2020)
    assert len(res) == 2
    assert book in res
    assert magazine in res


def test_library_search6():
    library = Library()
    book = Book("Book", "Author", 2020, "Genre", "107")
    library.add_book(book)
    res = library.search_year(1999)
    assert len(res) == 0


def test_book_repr():
    book = Book("Book Title", "Author Name", 1999, "Genre Type", "ISBN123")
    res = repr(book)
    assert "Book Title" in res
    assert "Author Name" in res
    assert "1999" in res
    assert "Genre Type" in res
    assert "ISBN123" in res


def test_magazine_repr():
    magazine = Magazine("Magazine Title", 2025, "Theme Name", "ISBN456")
    res = repr(magazine)

    assert "Magazine Title" in res
    assert "2025" in res

    assert "Theme Name" in res
    assert "ISBN456" in res





def test_player_repr():
    player = Player("Player Name")
    res = repr(player)
    assert "Player Name" in res
    assert "Фишки: 20" in res
    assert "ЖИВ" in res


def test_goose_repr():
    goose = Goose("Goose Name")
    res = repr(goose)
    assert "Goose Name" in res
    assert "украл фишек: 0" in res
    assert "ЖИВ" in res


def test_register_player():
    casino = Casino("Test Casino")
    player = Player("New Player")
    res = casino.register_player(player)
    assert res == 0

    assert len(casino.players) == 1
    assert player in casino.players


def test_bookcollection_add_item():
    collection = BookCollection()
    book = Book("Book", "Author", 2000, "Genre", "108")
    res = collection.add_item(book)
    

    assert res == 0
    assert len(collection) == 1




def test_bookcollection_remove_item():
    collection = BookCollection()
    book = Book("Book", "Author", 2000, "Genre", "109")
    collection.add_item(book)
    res = collection.remove_item(book)
    assert res == 0
    assert len(collection) == 0


def test_bookcollection_remove_nonexistent_item():
    collection = BookCollection()
    book = Book("Book", "Author", 2000, "Genre", "110")


    res = collection.remove_item(book)
    assert res == 1


def test_bookcollection_getitem():
    collection = BookCollection()
    book1 = Book("Book1", "Author", 2000, "Genre", "111")
    book2 = Book("Book2", "Author", 2001, "Genre", "112")
    collection.add_item(book1)
    collection.add_item(book2)
    assert collection[0] == book1
    assert collection[1] == book2


def test_bookcollection_len():
    collection = BookCollection()
    book1 = Book("Book1", "Author", 2000, "Genre", "113")
    book2 = Book("Book2", "Author", 2001, "Genre", "114")


    assert len(collection) == 0

    collection.add_item(book1)

    assert len(collection) == 1
    collection.add_item(book2)


    assert len(collection) == 2



def test_bookcollection_iter():
    collection = BookCollection()
    book1 = Book("Book1", "Author", 2000, "Genre", "115")
    book2 = Book("Book2", "Author", 2001, "Genre", "116")
    collection.add_item(book1)
    collection.add_item(book2)
    items = list(collection)


    assert len(items) == 2
    assert book1 in items
    assert book2 in items


def test_indexdict_update_index():
    index = IndexDict()
    book = Book("Book", "Author", 2000, "Genre", "117")
    res = index.update_index(book)
    assert res == 0
    assert "117" in index.isbn_dict
    assert "Author" in index.author_dict
    assert 2000 in index.year_dict




def test_indexdict_remove_index():
    index = IndexDict()


    book = Book("Book", "Author", 2000, "Genre", "118")
    index.update_index(book)
    res = index.remove_index(book)
    

    assert res == 0
    assert "118" not in index.isbn_dict
    assert "Author" not in index.author_dict
    assert 2000 not in index.year_dict


def test_indexdict_getitem():
    index = IndexDict()

    book = Book("Book", "Author", 2000, "Genre", "119")
    index.update_index(book)
    res1 = index["119"]
    res2 = index["Author"]
    res3 = index[2000]
    
    assert len(res1) == 1
    assert len(res2) == 1
    assert len(res3) == 1


def test_indexdict_len():
    idx = IndexDict()
    book1 = Book("Book1", "Author1", 2000, "Genre", "120")
    book2 = Book("Book2", "Author2", 2001, "Genre", "121")
    assert len(idx) == 0
    idx.update_index(book1)
    assert len(idx) == 1
    idx.update_index(book2)

    assert len(idx) == 2



def test_goose_add():
    goose1 = Goose("Goose1")
    goose2 = Goose("Goose2")


    goose1.stolen_chips = 10
    goose2.stolen_chips = 5
    res = goose1 + goose2
    
    assert res == 15




def test_goosecollection_add_goose():
    collection = GooseCollection()
    goose = Goose("Goose")
    res = collection.add_goose(goose)


    assert res == 0
    assert len(collection) == 1


def test_goosecollection_remove_goose():
    collection = GooseCollection()
    goose = Goose("Goose")
    collection.add_goose(goose)

    res = collection.remove_goose(goose)


    assert res == 0
    assert len(collection) == 0


def test_goosecollection_getitem():
    collection = GooseCollection()
    goose1 = Goose("Goose1")
    goose2 = Goose("Goose2")
    collection.add_goose(goose1)
    collection.add_goose(goose2)
    assert collection[0] == goose1
    assert collection[1] == goose2



def test_goosecollection_len():
    collection = GooseCollection()

    goose1 = Goose("Goose1")

    goose2 = Goose("Goose2")
    assert len(collection) == 0
    collection.add_goose(goose1)


    assert len(collection) == 1
    collection.add_goose(goose2)
    assert len(collection) == 2




def test_playercollection_add_player():
    collection = PlayerCollection()
    player = Player("Player")
    res = collection.add_player(player)
    assert res == 0
    assert len(collection) == 1


def test_playercollection_remove_player():
    collection = PlayerCollection()
    player = Player("Player")
    collection.add_player(player)
    res = collection.remove_player(player)
    assert res == 0
    assert len(collection) == 0


def test_playercollection_getitem():
    collection = PlayerCollection()
    player1 = Player("Player1")
    player2 = Player("Player2")
    collection.add_player(player1)
    collection.add_player(player2)
    assert collection[0] == player1
    assert collection[1] == player2



def test_playercollection_len():
    collection = PlayerCollection()
    player1 = Player("Player1")
    player2 = Player("Player2")
    assert len(collection) == 0
    collection.add_player(player1)
    assert len(collection) == 1
    collection.add_player(player2)
    assert len(collection) == 2








def test_chipbalancedict_setitem_getitem():
    balances = ChipBalanceDict()
    balances["Player1"] = 100

    balances["Player2"] = 200
    assert balances["Player1"] == 100


    assert balances["Player2"] == 200





def test_chipbalancedict_len():
    balances = ChipBalanceDict()
    assert len(balances) == 0

    balances["Player1"] = 100
    assert len(balances) == 1


    balances["Player2"] = 200
    assert len(balances) == 2


def test_chipbalancedict_delitem():
    balances = ChipBalanceDict()
    balances["Player1"] = 100
    
    del balances["Player1"]
    
    assert "Player1" not in balances
    assert len(balances) == 0

def test_chipbalancedict_update():
    balances = ChipBalanceDict()
    res = balances.update("Player1", 150)
    assert res == 0
    assert balances["Player1"] == 150



def test_goosecollection_alive_geese():
    collection = GooseCollection()
    goose1 = Goose("Goose1")

    goose2 = Goose("Goose2")

    goose2.is_alive = False
    collection.add_goose(goose1)
    collection.add_goose(goose2)
    alive = collection.get_alive_geese()
    assert len(alive) == 1


    assert goose1 in alive
    assert goose2 not in alive




def test_playercollection_alive_players():
    collection = PlayerCollection()
    player1 = Player("Player1")

    player2 = Player("Player2")
    player2.is_alive = False
    collection.add_player(player1)
    collection.add_player(player2)
    alive = collection.get_alive_players()
    assert len(alive) == 1
    assert player1 in alive
    assert player2 not in alive



def test_item_init():
    item = Item("ID001", "Item Title", 2020)
    assert item.id == "ID001"
    assert item.title == "Item Title"
    assert item.year == 2020

    assert item.in_library == True


def test_bookcollection_repr():
    collection = BookCollection()
    repr(collection)

def test_goosecollection_repr():
    collection = GooseCollection()
    repr(collection)


def test_playercollection_repr():
    collection = PlayerCollection()
    repr(collection)



def test_chipbalancedict_repr():
    balances = ChipBalanceDict()
    repr(balances)


def test_casino_init():
    casino = Casino("My Casino")
    assert casino.name == "My Casino"
    assert len(casino.geese) == 0
    assert len(casino.players) == 0
    assert len(casino.balances) == 0




def test_indexdict_update_index3():
    index = IndexDict()
    magazine = Magazine("Magazine", 2020, "Theme", "124")
    
    res = index.update_index(magazine)
    
    assert res == 0
    assert "124" in index.isbn_dict
    assert 2020 in index.year_dict
    assert "Author" not in index.author_dict


def test_indexdict_remove_index3():
    index = IndexDict()
    magazine = Magazine("Magazine", 2020, "Theme", "125")
    index.update_index(magazine)
    
    res = index.remove_index(magazine)
    
    assert res == 0
    assert "125" not in index.isbn_dict
    assert 2020 not in index.year_dict




def test_indexdict_getitem3():
    index = IndexDict()
    res = index["nonexistent"]
    assert res == []



def test_player_panic2():
    player = Player("Player")
    res = player.panic()
    assert res != -1



def test_goose_steal_chips2():
    player = Player("Player")
    goose = Goose("Goose")
    res = goose.steal_chips(player)
    assert res != -1



def test_library_add_book2():
    library = Library()
    res = library.add_book(None)
    assert res == -1



def test_library_remove_book2():
    library = Library()
    res = library.remove_book(None)
    assert res == -1


def test_bookcollection_add_item2():
    collection = BookCollection()
    res = collection.add_item(None)
    assert res == -1


def test_bookcollection_remove_item2():
    collection = BookCollection()
    res = collection.remove_item(None)
    assert res == -1


def test_indexdict_update_index2():
    index = IndexDict()
    res = index.update_index(None)
    assert res == 0


def test_indexdict_remove_index2():
    index = IndexDict()
    res = index.remove_index(None)
    assert res == -1


def test_goosecollection_add_goose2():
    collection = GooseCollection()
    res = collection.add_goose(None)
    assert res == 0



def test_goosecollection_remove_goose2():
    collection = GooseCollection()
    res = collection.remove_goose(None)
    assert res == -1





def test_playercollection_add_player2():
    collection = PlayerCollection()
    res = collection.add_player(None)
    assert res == 0


def test_playercollection_remove_player2():
    collection = PlayerCollection()
    res = collection.remove_player(None)
    assert res == -1
