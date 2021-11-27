from fastapi import APIRouter,HTTPException
from starlette.responses import JSONResponse
from uuid import uuid4 as uuid
from models import Item


router = APIRouter()
fridge=[]

@router.get('/')
def get_items():
    return JSONResponse(fridge)

@router.get('/{item_id}')
def get_item(item_id:str):
    for item in fridge:
        if item["key"] == item_id:
            JSONResponse(item)           
    raise HTTPException(status_code=404, detail='Item Not found')


@router.delete('/{item_id}')
def use_item(item_id:str,quantity:int):

    for i_item,item in enumerate(fridge):
            if item["key"] == item_id:
                if item["quantity"] >= quantity:
                    fridge[i_item]["quantity"] -= quantity
                    return JSONResponse({"message":  item["name"] + " has been used. %d left." %item["quantity"]})
                else:
                    return JSONResponse({"message":  item["name"] + " quantity is insufficient. %d left." %item["quantity"]})
                
    raise HTTPException(status_code=404, detail='Item Not found')

@router.put('/')
def updated_post(item: Item):
    for i_item,item_f in enumerate(fridge):
        if item_f["key"] == item.key:
            fridge[i_item]["quantity"] = item.quantity
            return JSONResponse({"message":  item["name"] + " has been updated."})
    item.key=str(uuid())
    fridge.append(item.dict())
    return JSONResponse(fridge[-1])
