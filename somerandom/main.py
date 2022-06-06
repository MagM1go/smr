from .ext.endpoints import (
    ANIMALS,
    FACTS,
    IMAGES,
    ANIME,
    MISC,
    MISC_LYRICS,
    MISC_BASE64,
    MISC_BINARY,
    MISC_POKEDEX,
    MISC_MINECRAFT,
    MISC_BOT_TOKEN,
    MISC_CHAT_BOT,
    OVERLAYS,
    FILTERS,
    FILTERS_BRIGHTNESS,
    FILTERS_THRESHOLD,
    FILTERS_COLOR,
    CANVAS_MISC,
    CANVAS_MISC_FAKE_YOUTUBE_COMMENT,
    CANVAS_MISC_FAKE_TWEET,
    CANVAS_MISC_ITS_SO_STUPID,
    CANVAS_MISC_COLOR_PREVIEW,
    CANVAS_MISC_RGB,
    WELCOME_IMAGE,
    PREMIUM_AMONGUS,
    PREMIUM_PETPET,
    PREMIUM_WELCOME_IMAGE,
    PREMIUM_RANK_CARD,
)
from .ext.internal.requester import Requester
from .ext.internal.route import Route

GET = "GET"

class SomeRandomApi:

    def __init__(self, key: str = ''):
        self.key = key
        self.requester = Requester()

    async def create_request(self, path: str) -> str:
        return await self.requester.request(
            route=Route(method='GET', path=path)
        )

    async def anime(self, action: str) -> str:
        anime = ANIME.format(action=action)
        return await self.create_request(anime)

    async def animal(self, animal: str) -> str:
        animal = ANIMALS.format(animal=animal)
        return await self.create_request(animal)

    async def fact(self, fact: str) -> str:
        fact = FACTS.format(fact=fact)
        return await self.create_request(fact)

    async def image(self, image: str) -> str:
        img = IMAGES.format(image_name=image)
        return await self.create_request(img)
    
    async def misc(self, misc: str) -> str:
        misc = MISC.format(misc_name=misc)
        return await self.create_request(misc)

    async def lyrics(self, title: str, cancer: str) -> str:
        lyrics = MISC_LYRICS.format(title=title, cancer=cancer)
        return await self.create_request(lyrics)

    async def base64(self, encode: str, decode: str) -> str:
        base64 = MISC_BASE64.format(encode=encode, decode=decode)
        return await self.create_request(base64)

    async def binary(self, encode: str, decode: str) -> str:
        binary = MISC_BINARY.format(encode=encode, decode=decode)
        return await self.create_request(binary)
    
    async def pokedex(self, pokemon: str, dym: str) -> str:
        pokedex = MISC_POKEDEX.format(pokemon=pokemon, dym=dym, key=self.key)
        return await self.create_request(pokedex)

    async def minecraft(self, username: str) -> str:
        mc = MISC_MINECRAFT.format(username=username)
        return await self.create_request(mc)
    
    async def bot_token(self, _id: str) -> str:
        get_id = MISC_BOT_TOKEN.format(_id=_id)
        return await self.create_request(get_id)

    async def chat_bot(self, message: str) -> str:
        _message = MISC_CHAT_BOT.format(message=message, key=self.key)
        return await self.create_request(_message)
    
    async def overlay(self, overlay: str, avatar: str) -> str:
        _overlay = OVERLAYS.format(overlay=overlay, avatar=avatar, key=self.key)
        return await self.create_request(_overlay)
    
    async def filters(self, _filter: str, avatar: str) -> str:
        set_filter = FILTERS.format(_filter=_filter, avatar=avatar, key=self.key)
        return await self.create_request(set_filter)

    async def brightness(self, brightness: str, avatar: str) -> str:
        filter_brightness = FILTERS_BRIGHTNESS.format(brightness=brightness, avatar=avatar, key=self.key)
        return await self.create_request(filter_brightness)

    async def threshold(self, threshold: str, avatar: str) -> str:
        threshold = FILTERS_THRESHOLD.format(threshold=threshold, avatar=avatar, key=self.key)
        return await self.create_request(threshold)

    async def color(self, color: str, avatar: str) -> str:
        _color = FILTERS_COLOR.format(color=color, avatar=avatar, key=self.key)
        return await self.create_request(_color)

    async def canvas_misc(self, misc: str, avatar: str) -> str:
        canvas = CANVAS_MISC.format(misc=misc, avatar=avatar, key=self.key)
        return await self.create_request(canvas)

    async def youtube_comment(self, comment: str, avatar: str, username: str) -> str:
        yt_comment = CANVAS_MISC_FAKE_YOUTUBE_COMMENT.format(
            comment=comment, avatar=avatar, username=username, key=self.key
        )
        return await self.create_request(yt_comment)

    async def tweet(self, avatar: str, display_name: str, username: str, comment: str):
        twitter = CANVAS_MISC_FAKE_TWEET.format(
            avatar=avatar, display_name=display_name, username=username, comment=comment, key=self.key
        )
        return await self.create_request(twitter)

    async def stupid(self, avatar: str, dog: str) -> str:
        its_so_stupid = CANVAS_MISC_ITS_SO_STUPID.format(avatar=avatar, dog=dog, key=self.key)
        return await self.create_request(its_so_stupid)

    async def color_preview(self, hex_color: str) -> str:
        color = CANVAS_MISC_COLOR_PREVIEW.format(hex_color=hex_color, key=self.key)
        return await self.create_request(color)

    async def rgb(self, rgb: str) -> str:
        rgb_to_hex_or_hex_to_rgb_im_tired_help_me_please = CANVAS_MISC_RGB.format(rgb=rgb.replace(' ', ''), key=self.key)
        return await self.create_request(rgb_to_hex_or_hex_to_rgb_im_tired_help_me_please)

    async def welcome_image(
        self, name: str, welcome_type: str, avatar: str, 
        username: str, discriminator: str, guild_name: str,
        text_color: str, member_count: str
    ) -> str:
        welcomer = WELCOME_IMAGE.format(
            name=name, welcome_type=welcome_type, avatar=avatar,
            username=username, discriminator=discriminator, guild_name=guild_name,
            text_color=text_color, member_count=member_count, key=self.key
        )
        return await self.create_request(welcomer)

    async def amongsus(self, avatar: str, username: str, imposter: str = '') -> str:
        amongus = PREMIUM_AMONGUS.format(avatar=avatar, username=username, key=self.key, imposter=imposter)
        return await self.create_request(amongus)

    async def petpet(self, avatar: str) -> str:
        petpet_gif = PREMIUM_PETPET.format(avatar=avatar)
        return await self.create_request(petpet_gif)

    async def premium_welcome_image(
        self, welcome_type: str, avatar: str, bg: str,
        username: str, discriminator: str, guild_name: str,
        text_color: str, member_count: str
    ) -> str:
        welcomer = PREMIUM_WELCOME_IMAGE.format(
            bg=bg, welcome_type=welcome_type, avatar=avatar, 
            username=username, discriminator=discriminator, guild_name=guild_name,
            text_color=text_color, member_count=member_count, key=self.key
        )
        return await self.create_request(welcomer)

    async def rank_card(
        self, avatar: str, username: str, discriminator: str,
        level: str, cxp: str, nxp: str, rank: str, bg: str,
        cbg: str, ctext: str, ctag: str, ccxp: str, cbar: str
    ) -> str:
        card = PREMIUM_RANK_CARD.format(
            avatar=avatar, username=username, discriminator=discriminator,
            level=level, cxp=cxp, nxp=nxp, rank=rank, bg=bg,
            cbg=cbg, ctext=ctext, ctag=ctag, ccxp=ccxp, cbar=cbar
        )
        return await self.create_request(card)
