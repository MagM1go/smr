from smr_py import smr_sync


smr = smr_sync.SMR_client()

print(smr.get_point(
                    category="canvas",
                    name="invert",
                    path="?avatar=https://images-ext-2.discordapp.net/external/0DUf6d_FzJSMhsAXEAoYjtGVbdtvbOa6eM7IeBn6m7g/https/cdn.discordapp.com/avatars/598387707311554570/5eb2fad66a96e41fcb514df8d632a354.png"
    ))
