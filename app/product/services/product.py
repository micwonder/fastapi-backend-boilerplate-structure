import json
import random
import string
from typing import List, Optional

# Migrate to other file

from sqlalchemy import and_, select

from app.business_setting.models.business_setting import BusinessSetting
from app.product.models import Product
from app.user.models.user import User
from app.addon.models.addon import Addon
from app.product_tax.models.product_tax import ProductTax
from app.flash_deal_product.models.flash_deal_product import FlashDealProduct
from app.product_translation.models.product_translation import ProductTranslation
from app.product_stock.models.product_stock import ProductStock
from core.exceptions import CustomException, ForbiddenException, NotFoundException
from core.db import Transactional, session


class ProductService:
    def __init__(self):
        ...

    async def get_product_list(
        self,
        page: int,
        size: int,    # optional[int]
        order_by: str,
        desc: bool,
        accept_language: Optional[str],
    ) -> List[Product]:
        try:
            if size > 100:
                size = 100
            offset = page*size
            if desc:
                query = select(Product).order_by(getattr(Product, order_by).desc())
            else:
                query = select(Product).order_by(getattr(Product, order_by))
            query = query.offset(offset).limit(size)
            result = await session.execute(query)
            result = result.scalars().all()
            for val in result:
                if not val.added_by:
                    val.added_by = "----------Not set----------"
            return result
        except CustomException("Order_by__WRONG_FIELD_INPUT") as exception:
            raise exception

    async def get_product(
        self,
        id: int,
        accept_language: Optional[str],
    ) -> Product:
        query = select(Product).where(Product.id == id)
        result = await session.execute(query)

        return result.scalars().all()[0]

    @Transactional()
    async def add_product(
        self,
        name: str,
        added_by: str,
        user_id: int,
        category_id: int,
        brand_id: int,
        photos: str,
        thumbnail_img: str,
        video_provider: str,
        video_link: str,
        tags: str,
        description: str,
        unit_price: float,
        purchase_price: float,
        variant_product: int,
        choice_no: list,
        choice_data: dict,
        colors: str,
        variations: str,
        todays_deal: int,
        button: str,
        approved: bool,
        stock_visibility_state: str,
        cash_on_delivery: bool,
        featured: int,
        seller_featured: int,
        current_stock: int,
        unit: str,
        min_qty: int,
        low_stock_quantity: int,
        discount: float,
        discount_type: str,
        discount_start_date: int,
        discount_end_date: int,
        tax_id: list,
        tax: list,
        tax_type: str,
        flash_deal_id: int,
        translations: list,
        shipping_type: str,
        shipping_cost: str,
        is_quantity_multiplied: bool,
        est_shipping_days: int,
        num_of_sale: int,
        meta_title: str,
        meta_description: str,
        meta_img: str,
        pdf: str,
        slug: str,
        rating: float,
        barcode: str,
        digital: int,
        auction_product: int,
        file_name: str,
        file_path: str,
        accept_language: Optional[str],
    ) -> str:
        if not name or not category_id or not unit or not tags or not min_qty or not unit_price or not current_stock or not thumbnail_img:
            return

        product = Product(name=name, added_by=added_by, user_id=user_id, category_id=category_id, brand_id=brand_id, photos=photos, thumbnail_img=thumbnail_img, video_provider=video_provider, video_link=video_link, tags=tags, description=description, unit_price=unit_price, purchase_price=purchase_price, variant_product=variant_product, attributes="", choice_options="", colors=colors, variations=variations, todays_deal=todays_deal, published=1, approved=approved, stock_visibility_state=stock_visibility_state, cash_on_delivery=cash_on_delivery, featured=featured, seller_featured=seller_featured, current_stock=current_stock, unit=unit, min_qty=min_qty, low_stock_quantity=low_stock_quantity, discount=discount, discount_type=discount_type, discount_start_date=discount_start_date, discount_end_date=discount_end_date, tax=0, tax_type=tax_type, shipping_type=shipping_type, shipping_cost=shipping_cost, is_quantity_multiplied=is_quantity_multiplied, est_shipping_days=est_shipping_days, num_of_sale=num_of_sale, meta_title=meta_title, meta_description=meta_description, meta_img=meta_img, pdf=pdf, slug=slug, rating=rating, barcode=barcode, digital=digital, auction_product=auction_product, file_name=file_name, file_path=file_path)

        # validation of laravel => middleware of bolilerplate
        result = await session.execute(
            select(User).where(
                User.id == user_id
            )
        )
        user = result.scalars().first()

        if not user:
            raise NotFoundException("Add_product__USER_NOT_FOUND")

        if user.user_type == "seller":
            product.user_id = user_id
            result = await session.execute(
                select(BusinessSetting).where(
                    BusinessSetting.type == "product_approve_by_admin"
                )
            )
            business_setting = result.value
            if business_setting == "1":
                product.approved = 0
        else:
            result = await session.execute(
                select(User).where(User.user_type == "admin")
            )
            user = result.scalars().first()
            if not user:
                raise NotFoundException("Add_product_ADMIN_USER_NOT_FOUND")
            product.user_id = user.id

        # return !($activation == null);
        # result = await session.execute (
        #    select(addons)
        # )

        # tags is array()
        # take care of groups
        # is there date_range?
        result = await session.execute(
            select(Addon).where(
                Addon.unique_identifier == 'club_point'
            )
        )
        addon = result.scalars().first()
        earn_point = 0
        if addon  and addon.activated:
            earn_point = 1

        if shipping_type:
            if shipping_type == 'free':
                product.shipping_cost = 0
            elif shipping_type == 'flat_shipping_cost':
                product.shipping_cost = shipping_cost
            elif shipping_type == 'product_wise':
                product.shipping_cost = json.JSONEncoder().encode(shipping_type)

        if is_quantity_multiplied:
            product.is_quantity_multiplied = 1
        if not meta_title:
            product.meta_title = name
        if not meta_description:
            product.meta_description = description
        if not meta_img:
            product.meta_img = thumbnail_img

        # pdf store uploads/products/pdf

        if not slug:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(5))
            product.slug = name.join(result_str)

        # choice_options
        options = []
        product.attributes = json.JSONEncoder().encode([])
        if choice_no :
            product.attributes = json.JSONEncoder().encode(choice_no)
            item = {}
            for no in choice_no:
                choice_index = 'choice_options_' + str(no)
                item['attribute_id'] = no
                item['values'] = choice_data[choice_index]
                options.append(item)
            product.choice_options = json.JSONEncoder().encode(options)

        if button == 'Save & Unpublish' or button == 'Save As Draft':
            product.published = 0

        session.add(product)
        await session.flush()

        # VAT & Tax
        if tax_id :
            for key, val in enumerate(tax_id):
                product_tax = ProductTax(
                    product_id=product.id, tax_id=val, tax=tax[key], tax_type=tax_type)
                session.add(product_tax)

        # Flash Deal
        if flash_deal_id :
            flash_deal_product = FlashDealProduct(
                flash_deal_id=flash_deal_id, product_id=product.id, discount=discount, discount_type=discount_type)
            session.add(flash_deal_product)
        # Combinations start
        # Generates the combinations of customer choice options
        # Combinations end

        combinations = 0
        if not combinations:
            product_stock = ProductStock(
                product_id=product.id, variant="", qty=current_stock)
            session.add(product_stock)

        # Product Translations
        if translations :
            for trans_data in translations:
                result = await session.execute(
                    select(ProductTranslation).where(
                        and_(ProductTranslation.lang == trans_data['locale'],
                             ProductTranslation.name == trans_data['name']
                        )
                    )
                )
                product_translation = result.scalars().first()
                if not product_translation:
                    product_translation = ProductTranslation(
                        product_id=product.id, name=trans_data['name'], lang=trans_data['locale'])
                    session.add(product_translation)
                else:
                    product_translation.name = trans_data['name']
                    session.commit()

        # We have to flash success message then route to back
        return "back"

    @Transactional()
    async def update_product(
        self,
        id: int,
        name: str,
        user_id: int,
        category_id: int,
        thumbnail_img: str,
        tags: str,
        description: str,
        unit_price: float,
        choice_no: list,
        choice_data: dict,
        button: str,
        current_stock: int,
        unit: str,
        min_qty: int,
        shipping_type: str,
        shipping_cost: str,
        is_quantity_multiplied: bool,
        meta_title: str,
        meta_description: str,
        meta_img: str,
        slug: str,
        accept_language: Optional[str],
    ) -> str:

        result = await session.execute(
            select(Product).where(
                and_(Product.id == id, Product.name == name)
            )
        )
        product = result.scalars().first()
        if not product:
            raise NotFoundException("Update_product__PRODUCT_NOT_FOUND")

        if not name or not category_id or not unit or not tags or not min_qty or not unit_price or not current_stock or not thumbnail_img:
            return

        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalars().first()
        if user.user_type != 'admin':
            raise ForbiddenException

        # validation of laravel => middleware of bolilerplate

        if user.user_type == "seller":
            product.user_id = user_id
            result = await session.execute(
                select(BusinessSetting).where(
                    BusinessSetting.type == "product_approve_by_admin"
                )
            )
            business_setting = result.value
            if business_setting == "1":
                product.approved = 0
        else:
            result = await session.execute(
                select(User).where(User.user_type == "admin")
            )
            user = result.scalars().first()
            if not user:
                raise NotFoundException("Update_product__ADMIN_USER_NOT_FOUND")
            product.user_id = user.id

        # return !($activation == null);
        # result = await session.execute (
        #    select(addons)
        # )

        # tags is array()
        # take care of groups
        # is there date_range?
        result = await session.execute(
            select(Addon).where(Addon.unique_identifier == 'club_point')
        )
        addon = result.scalars().first()
        earn_point = 0
        if addon  and addon.activated:
            earn_point = 1

        if shipping_type :
            if shipping_type == 'free':
                product.shipping_cost = 0
            elif shipping_type == 'flat_shipping_cost':
                product.shipping_cost = shipping_cost
            elif shipping_type == 'product_wise':
                product.shipping_cost = json.JSONEncoder.encode(shipping_type)

        if is_quantity_multiplied :
            product.is_quantity_multiplied = 1
        if not meta_title:
            product.meta_title = name
        if not meta_description:
            product.meta_description = description
        if not meta_img:
            product.meta_img = thumbnail_img

        # pdf store uploads/products/pdf

        if not slug:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(5))
            product.slug = name.join(result_str)

        # choice_no part
        options = []
        product.attributes = json.JSONEncoder.encode([])
        if choice_no :
            product.attributes = json.JSONEncoder.encode(choice_no)
            item = {}
            for no in choice_no:
                choice_index = 'choice_options_' + str(no)
                item['attribute_id'] = no
                item['values'] = choice_data[choice_index]
                options.append(item)
            product.choice_options = json.JSONEncoder.encode(options)

        if button == 'Save & Unpublish' or button == 'Save As Draft':
            product.published = 0

        # VAT & Tax
        # Flash Deal
        # Combinations start
        # Generates the combinations of customer choice options
        # Combinations end
        # Product Translations

        session.add(product)

        # We have to flash success message then route to back
        return "back"

    async def remove(
        self,
        id: int,
        name: str,
        accept_language: Optional[str],
    ) -> None:
        result = await session.execute(
            select(Product).where(Product.id == id)
        )
        product = result.scalars().first()
        if not product:
            raise NotFoundException("Delete__PRODUCT_NOT_FOUND")

        product.delete()
        session.commit()
