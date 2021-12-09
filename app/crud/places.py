from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, descriptor_props
from app.model.place import PLace as PlaceModel
from app.schemas.place import PlaceCreate, PlaceUpdate, Place

#Create, Read, Update, Delete
#Read un sólo lugar por el id, obetener todos los lugares
"""Obtiene un place por el id"""
def get(db:Session, place_id:int) -> PlaceModel:
    return db.query(PlaceModel).filter(PlaceModel.id == place_id).first()

"""Obtener todos los sitios"""
def get_places(db:Session, skip: int = 0, limit: int = 10):
    return db.query(PlaceModel).offset(skip).limit(limit).all()

"""Crear un sitio"""
def create_place(db:Session, place: PlaceCreate):
    db_place = PlaceModel(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

"""Actualizar un sitio"""
def update_place(db:Session, *,db_obj:Place, obj_in: PlaceUpdate)-> Place:
   obj_data = jsonable_encoder(db_obj)
   if isinstance(obj_in,dict):
       update_data = obj_in
   else:
       update_data = obj_in.dict(exclude_unset=True)
   for field in obj_data:
       if field in update_data:
           setattr(db_obj,field, update_data[field])
 
   db.add(db_obj)
   db.commit()
   db.refresh(db_obj)
   return db_obj

"""Eliminar un sitio"""
def delete_place (db:Session, *, id: int)->Place:
   obj = db.query(Place).get(id)
   db.delete(obj)
   db.commit()
   return obj
