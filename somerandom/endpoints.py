import typing
from dataclasses import dataclass


@dataclass
class Animal:
    animal: str

    def get_path(self):
        return f"/animal/{self.animal}"

@dataclass
class Facts:
    name: str

    def get_path(self):
        return f"/facts/{self.name}"


@dataclass
class Image:
    name: str

    def get_path(self):
        return f"/img/{self.name}"

@dataclass
class Anime:
    action: str

    def get_path(self):
        return f"/animu/{self.action}"

@dataclass
class Misc:
    name: typing.Optional[str] = ''

    def get_path(self) -> str:
        return f'/{self.name}'
    
    @dataclass
    class Lyrics:
        title: str
        cancer: typing.Optional[str] = ''

        def get_path(self):
            return f"/lyrics?title={self.title}&cancer={self.cancer}"
        
    @dataclass
    class Base64:
        encode: str
        decode: str

        def get_path(self):
            return f"/base64?encode={self.encode}&decode={self.decode}"

    @dataclass
    class Binary:
        encode: str
        decode: str

        def get_path(self):
            return f"/binary?encode={self.encode}&decode={self.decode}"

    @dataclass
    class Pokedex:
        pokemon: str
        dym: typing.Optional[str] = ''
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/pokedex?pokemon={self.pokemon}&dym={self.decode}&key={self.key}"

    @dataclass
    class Minecraft:
        username: str

        def get_path(self):
            return f"/mc/{self.username}"

    @dataclass
    class DiscordBotToken:
        bot_id: str

        def get_path(self):
            return f"/mc/{self.username}"
    
    @dataclass
    class ChatBot:
        message: str
        key: str

        def get_path(self):
            return f"/chatbot/message={self.message}&key={self.key}"

@dataclass
class Overlays:
    avatar: str
    overlay: str
    key: typing.Optional[str] = ''

    def get_path(self):
        return f"/canvas/{self.overlay}?avatar={self.avatar}&key={self.key}"

@dataclass
class Filters:
    avatar: str
    key: typing.Optional[str] = ''
    _filter: typing.Optional[str] = ''

    def get_path(self):
        return f"/canvas/{self._filter}?avatar={self.avatar}&key={self.key}"

    @dataclass
    class BrightnessFilter:
        avatar: str
        key: typing.Optional[str] = ''
        brightness: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/brightness?avatar={self.avatar}&key={self.key}&brightness={self.brightness}"
    
    @dataclass
    class ThresholdFilter:
        avatar: str
        key: typing.Optional[str] = ''
        threshold: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/threshold?avatar={self.avatar}&key={self.key}&threshold={self.threshold}"

    @dataclass
    class CololFilter:
        avatar: str
        color: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/color?avatar={self.avatar}&key={self.key}&color={self.threshold}"


@dataclass
class CanvasMisc:
    avatar: str
    misc: str
    key: typing.Optional[str] = ''

    def get_path(self):
        return f"/canvas/{self.misc}?avatar={self.avatar}&key={self.key}"

    @dataclass
    class FakeYoutubeComment:
        username: str
        comment: str
        avatar: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/youtube-comment?avatar={self.avatar}&username={self.username}&comment={self.comment}&key={self.key}"

    @dataclass
    class FakeTweet:
        username: str
        display_name: str
        avatar: str
        comment: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/tweet?avatar={self.avatar}&displayname={self.display_name}&username={self.username}&comment={self.comment}&key={self.key}"
    
    @dataclass
    class ItsSoStupid: # It's me ^-^
        avatar: str
        dog: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/its-so-stupid?avatar={self.avatar}&key={self.key}&dog={self.dog}"
    

    @dataclass
    class ColorPreview:
        hex_color: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/colorviewer?hex={self.hex_color}&key={self.key}"
    
    @dataclass
    class Hex:
        rgb: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/hex?rgb={self.rgb}&key={self.key}"

    @dataclass
    class Rgb:
        _hex: str
        key: typing.Optional[str] = ''

        def get_path(self):
            return f"/canvas/rgb?rgb={self._hex}&key={self.key}"


@dataclass
class WelcomeImages:
    name: str
    welcome_type: str
    avatar: str
    username: str
    discriminator: str
    guild_name: str
    textcolor: str
    member_count: str
    key: typing.Optional[str] = ''

    def get_path(self):
        return f"/welcome/img/1/stars2?name={self.name}" + \
               f"&type={self.welcome_type}&avatar={self.avatar}" + \
               f"&username={self.username}&discriminator={self.discriminator}" + \
               f"guildName={self.guild_name}&textcolor={self.textcolor}&memberCount={self.member_count}" + \
               f"&key={self.key}" # XDDD


@dataclass
class Premium:
    
    @dataclass
    class AmongSus:
        avatar: str
        username: str
        key: str
        imposter: typing.Optional[str] = ''

        def get_path(self):
            return f"/premium/amongus?avatar={self.avatar}&username={self.username}&key={self.key}&imposter={self.imposter}"
    
    @dataclass
    class Petpet:
        avatar: str
        key: str

        def get_path(self):
            return f"/premium/petpet?avatar={self.avatar}&key={self.key}"

    @dataclass
    class MoreCustomWelcomeImages:
        welcome_type: str
        avatar: str
        username: str
        discriminator: str
        guild_name: str
        textcolor: str
        member_count: str
        bg: str
        key: str

        def get_path(self):
            return f"/welcome/1?type={self.welcome_type}&avatar={self.avatar}" + \
                   f"&username={self.username}&discriminator={self.discriminator}" + \
                   f"guildName={self.guild_name}&textcolor={self.textcolor}&memberCount={self.member_count}" + \
                   f"&key={self.key}&bg={self.bg}"

    @dataclass
    class RankCard:
        username: str
        discriminator: str
        avatar: str
        level: str
        cxp: str
        nxp: str
        key: str
        rank: typing.Optional[str] = ''
        bg: typing.Optional[str] = ''
        cbg: typing.Optional[str] = ''
        ctext: typing.Optional[str] = ''
        ctag: typing.Optional[str] = ''
        ccxp: typing.Optional[str] = ''
        cbar: typing.Optional[str] = ''

        def get_path(self):
            return f"/premium/rankcard/1?avatar={self.avatar}" + \
                   f"&username={self.username}&discriminator={self.discriminator}" + \
                   f"&level={self.level}&cxp={self.cxp}&nxp={self.nxp}" + \
                   f"&key={self.key}&rank={self.rank}&bg={self.bg}&cbg={self.cbg}" + \
                   f"&ctext={self.ctext}&ctag={self.ctag}&ccxp={self.ccxp}" + \
                   f"&cbar={self.cbar}"
