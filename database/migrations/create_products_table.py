from sqlalchemy import Column, Boolean, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Products(Base):
    __tablename__ = "products"
    product_id = Column(String(255), primary_key=True)
    brand = Column(String(255))
    category = Column(String(255))
    color = Column(String(255))
    description = Column(String(255))
    gender = Column(String(255))
    name = Column(String(255))
    selling_price = Column(Integer())
    recommandable = Column(Boolean())
    sub_category = Column(String(255))
    sub_sub_category = Column(String(255))
    sub_sub_sub_category = Column(String(255))
    discount = Column(String(255))
    availablity = Column(String(255))
    target_group = Column(String(255))
    unit = Column(String(255))
    online_only = Column(Boolean())
    series = Column(String(255))
    sort = Column(String(255))
    type = Column(String(255))
    variant = Column(String(255))
    fragrance_type = Column(String(255))
    type_hair_care = Column(String(255))
    type_hair_color = Column(String(255))

    def __repr__(self):
        return 'id: {}'.format(self.product_id)