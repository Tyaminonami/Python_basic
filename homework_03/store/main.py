from fastapi import FastAPI
import Products as p


app = FastAPI(
    title="Kitchen Utensils Store"
)


@app.get("/")
def show_all_kind_of_products():
    return p.list_of_products


@app.get("/ping/")
def chek():
    return {"message": "pong"}


@app.post("/find/")
def find(x: str):
    if x == "Teapot":
        return p.list_of_teapot
    elif x == "Spoon":
        return p.list_of_spoon
    elif x == "Frying" or x == "Pan":
        return p.list_of_frying_pan
    else:
        return f"ERROR"


@app.post("/add/")
def add(which_list: str, product: dict):
    if which_list == "Teapot":
        p.list_of_teapot.append(product)
        return f"{product} successfully added in list of teapot" \
               f"{p.list_of_teapot}"
    elif which_list == "Spoon":
        p.list_of_spoon.append(product)
        return f"{product} successfully added in list of spoon" \
               f"{p.list_of_spoon}"
    elif which_list == "Frying" or list == "Pan":
        p.list_of_frying_pan.append(product)
        return f"{product} successfully added in list of frying pan" \
               f"{p.list_of_frying_pan}"
    else:
        return f"ERROR"






