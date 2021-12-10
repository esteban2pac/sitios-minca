from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import place
from app.crud import crud_place
from app.api import deps
 
router = APIRouter()
 
@router.get("/places/", response_model=List[place.Place])
def read_places(db: Session = Depends(deps.get_db),skip: int = 0,limit: int = 100,) -> Any:
 
    return crud_place.get_places(db,skip,limit)
 
@router.post("/places/", response_model=place.Place)
def create_item(*,db: Session = Depends(deps.get_db),place_in: place.PlaceCreate,) -> Any:
   place = crud_place.create_place(db=db,place=place_in)
   return place
 
@router.put("/places/{id}", response_model=place.Place)
def update_place(*,db: Session = Depends(deps.get_db),id: int,place_in: place.PlaceUpdate,) -> Any:
  
   placeInDB = crud_place.get(db=db, place_id=id)
   if not placeInDB:
       raise HTTPException(status_code=404, detail="Place not found")
  
   place = crud_place.update_place(db=db,db_obj=placeInDB,obj_in=place_in)
   return place
 
@router.get("/places/{id}", response_model=place.Place)
def read_place(*,db: Session = Depends(deps.get_db),id: int,) -> Any:
 
   place = crud_place.get(db=db, place_id=id)
   if not place:
       raise HTTPException(status_code=404, detail="Place not found")
   return place
 
@router.delete("/places/{id}", response_model=place.Place)
def delete_item(*,db: Session = Depends(deps.get_db),id: int,) -> Any:
 
   place = crud_place.get(db=db, place_id=id)
   if not place:
       raise HTTPException(status_code=404, detail="Place not found")
 
   place = crud_place.delete_place(db=db,id=id)
   return place