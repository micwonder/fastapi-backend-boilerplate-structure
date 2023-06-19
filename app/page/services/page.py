# from typing import Optional, List

from sqlalchemy import select

from app.page.models import Page
from core.db import Transactional, session
# from core.utils.token_helper import TokenHelper
from slugify import slugify

class PageService:
    def __init__(self):
        ...

    async def create_page(
            self,
            type: str,
            url: str,
            title: str,
            slug: str,
            content: str,
            meta_title: str,
            meta_description: str,
            keywords: str,
            meta_image: str,
            lang: str
    ):
        slug = slugify(slug)
        result = await session.execute(
            select(Page).where(
                Page.slug == slug
            )
        )
        page = result.scalars().first()
        if page:
            page = Page(type="custom_page", url=url, title=title, slug=slug, content=content, meta_image=meta_image, meta_title=meta_title, meta_description=meta_description, keywords=keywords, meta_image=meta_image, lang=lang)
            session.add(page)

            # call page_translation model
            
        else:
            pass    # flash('translate('Slug has been used already'))-> warning()


