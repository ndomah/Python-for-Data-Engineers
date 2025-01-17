from jdb.kv import KVStore
from vehicles.fourwheelers.hector import Hector
from vehicles.fourwheelers.car import Car


def get_hector(db):
    return Hector(**db.get("Hector"))


if __name__ == "__main__":
    h1 = Hector()
    h1.speed_up(40)

    c1 = Car()
    c1.speed_up(20)

    store = KVStore("E:/demo/jdb/my-kv_store")
    store.set("Hector", h1)
    store.set("Car", c1)
    store.save()

    h2 = get_hector(store)
    h2.show_state()

    print(str(store.key_count()))

    for key in store.keys():
        print("Key: {}, Value: {}".format(key, store.get(key)))

    store.delete("Hector")

    for key in store.keys():
        print("Key: {}, Value: {}".format(key, store.get(key)))
