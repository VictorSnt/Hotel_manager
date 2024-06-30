from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Tuple
from datetime import datetime, date, time
from decimal import Decimal


class RoomCategory(BaseModel):
    category_id: int
    description: str
    one_guest_price: Decimal
    two_guest_price: Decimal
    three_guest_price: Decimal
    four_guest_price: Decimal

    class Config:
        orm_mode = True


class Product(BaseModel):
    product_id: int
    description: str
    price: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Customer(BaseModel):
    GENDERS: List[Tuple[str, str]] = [
        ('Masc', 'Masc'),
        ('Fem', 'Fem')
    ]
    MARITAL_CHOICES: List[Tuple[str, str]] = [
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
        ('Viuvo(a)', 'Viuvo(a)'),
    ]
    customer_id: int
    full_name: Optional[str]
    birth_date: Optional[date]
    cpf: Optional[str]
    rg: Optional[str]
    gender: Optional[str]
    marital_status: Optional[str]
    partner: Optional[str]
    ocupation: Optional[str]
    ocupation_company_name: Optional[str]
    zip_code: Optional[str]
    address_street: Optional[str]
    address_number: Optional[str]
    address_ref: Optional[str]
    address_district: Optional[str]
    address_city: Optional[str]
    address_uf: Optional[str]
    phone: str
    cellphone: Optional[str]
    email: Optional[EmailStr]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Room(BaseModel):
    STATUS_CHOICES: List[Tuple[str, str]] = [
        ('L', 'L'),
        ('O', 'O'),
        ('S', 'S'),
        ('M', 'M'),
        ('R', 'R'),
    ]
    room_id: int
    room_number: str
    status: str
    category: RoomCategory
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Reservation(BaseModel):
    GUEST_QUANT: List[Tuple[str, str]] = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    room_reservation_id: int
    room: Room
    customer: Customer
    guest_quant: str
    open: bool
    days_quant: int
    checkin_date: date
    checkout_date: date
    checkin_time: Optional[time]
    checkout_time: Optional[time]
    hosting_price: Decimal
    total_hosting_price: Decimal
    total_bill: Decimal
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ProductConsume(BaseModel):
    product_consume_id: int
    room_reservation_id: Reservation
    room_id: Room
    product_id: Product
    qtproduct: int
    unit_price: Decimal
    total: Decimal
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class HotelReservation(BaseModel):
    id: int
    room_id: Room
    checkin_date: date
    customer_name: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
