from .internal.requester import Route


GET = "GET"

ANIMALS = "/animal/{animal}"
FACTS = "/facts/{fact}"
IMAGES = "/img/{image_name}"
ANIME = "/animu/{action}"

# Misc

MISC = "/{misc_name}"
MISC_LYRICS = "/lyrics?title={title}&cancer={cancer}"
MISC_BASE64 = "/base64?encode={encode}&decode={decode}"
MISC_BINARY = "/binary?encode={encode}&decode={decode}"
MISC_POKEDEX = "/pokedex?pokemon={pokemon}&dym={dym}&key={key}"
MISC_MINECRAFT = "/mc?username={username}"
MISC_BOT_TOKEN = "/bottoken?id={_id}"
MISC_CHAT_BOT = "/chatbot/message={message}&key={key}"

# Images
OVERLAYS = "/canvas/{overlay}?avatar={avatar}&key={key}"
FILTERS = "/canvas/{_filter}?avatar={avatar}&key={key}"
FILTERS_BRIGHTNESS = "/canvas/brightness?avatar={avatar}&key={key}&brightness={brightness}"
FILTERS_THRESHOLD = "/canvas/threshold?avatar={avatar}&key={key}&threshold={threshold}"
FILTERS_COLOR = "/canvas/color?avatar={avatar}&key={key}&color={color}"

# Canvas misc
CANVAS_MISC = "/canvas/{misc}?avatar={avatar}&key={key}"
CANVAS_MISC_FAKE_YOUTUBE_COMMENT = "/canvas/youtube-comment?avatar={avatar}&username={username}&comment={comment}&key={key}"
CANVAS_MISC_FAKE_TWEET = "/canvas/tweet?avatar={avatar}&displayname={display_name}&username={username}&comment={comment}&key={key}"
CANVAS_MISC_ITS_SO_STUPID = "/canvas/its-so-stupid?avatar={avatar}&key={key}&dog={dog}"
CANVAS_MISC_COLOR_PREVIEW = "/canvas/colorviewer?hex={hex_color}&key={key}"
CANVAS_MISC_RGB = "/canvas/hex?rgb={rgb}&key={key}"

# Welcome

WELCOME_IMAGE = "/welcome/img/1/stars2?name={name}" + \
                           "&type={welcome_type}&avatar={avatar}" + \
                           "&username={username}&discriminator={discriminator}" + \
                           "guildName={guild_name}&textcolor={text_color}&memberCount={member_count}" + \
                           "&key={key}"
# Premium
PREMIUM_AMONGUS = "/premium/amongus?avatar={avatar}&username={username}&key={key}&imposter={imposter}"
PREMIUM_PETPET = "/premium/petpet?avatar={avatar}&key={key}"
PREMIUM_WELCOME_IMAGE = "/welcome/1?type={welcome_type}&avatar={avatar}" + \
                                   "&username={username}&discriminator={discriminator}" + \
                                   "guildName={guild_name}&textcolor={textcolor}&memberCount={member_count}" + \
                                   "&key={key}&bg={bg}"
PREMIUM_RANK_CARD = "/premium/rankcard/1?avatar={avatar}" + \
                               "&username={username}&discriminator={discriminator}" + \
                               "&level={level}&cxp={cxp}&nxp={nxp}" + \
                               "&key={key}&rank={rank}&bg={bg}&cbg={cbg}" + \
                               "&ctext={ctext}&ctag={ctag}&ccxp={ccxp}" + \
                               "&cbar={cbar}"
