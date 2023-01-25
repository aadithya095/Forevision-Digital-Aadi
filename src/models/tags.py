from enum import Enum

class IdTypeSet(Enum):
    isrc = "ISRC"
    icpn = 'ICPN'
    grid = 'GRid'
    proprietary_id = 'ProprietaryId'

class PartyTypeSet(Enum):
    artist = 'Artist'
    contributor = 'Contributor'

class PartyRoleSet(Enum):
    main_artist = 'MainArtist'
    singer = "Singer"
    lyricist = "Lyricist"
    composer = "Composer"
    guitarist = "Guitarist"

class PlanSet(Enum):
    """
    Choices that are available to a user are
    Single Release Plan
    Album Release Plan

    It includes and plans that are given by the client
    """
    single = "Single"
    album = "Album"
