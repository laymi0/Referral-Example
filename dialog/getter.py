from module.database import Referral


async def getter(**_) -> dict:
    referrals = await Referral.filter()

    text = 'Your links:\n\n'
    links = []
    for ref in referrals:
        links.append(ref.name)
    return {"refferals": links[::-1], "text": text}



