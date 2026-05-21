from sqlalchemy.orm import Session
from app.models.products import Product
from app.schemas.producto_schema import ProductoCreate, ProductoBase

# Esta función busca a todos los productos que tenemos guardados en la lista de MySQL
def get_productos(db: Session):
    return db.query(Product).all()

# Esta sirve para buscar un solo producto usando su número de ID
def get_producto(db: Session, producto_id: int):
    return db.query(Product).filter(Product.id == producto_id).first()

# Aquí es donde ocurre la magia para guardar un nuevo producto que nos envíen
def create_producto(db: Session, item: ProductoCreate):
    db_producto = Product(
        nombre=item.nombre,
        categoria=item.categoria,
        cantidad=item.cantidad,
        precio=item.precio
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Esta función busca un producto por su ID y le cambia la información por la nueva
def update_producto(db: Session, producto_id: int, item: ProductoBase):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db_producto.nombre = item.nombre
        db_producto.categoria = item.categoria
        db_producto.cantidad = item.cantidad
        db_producto.precio = item.precio
        db.commit()
        db.refresh(db_producto)
    return db_producto

# Y esta última es para borrar un producto del inventario si ya no lo necesitamos
def delete_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
        return True
    return False