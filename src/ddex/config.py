"""
Author: iamu985
Github: https://github.com/iamu985

All the project level variables, methods and classes can be kept here to be made access easy.
"""
import os

ROOT_DIR = os.path.realpath(os.path.join(__file__, '..', '..', '..'))
RELEASE_NOTIFICATION_SCHEMA = 'docs/assets/ern/release-notification.xsd'

ReleaseTypeSet = {
        'Album',
        'AlertToneRelease',
        'AsPerContract',
        'AudioBookRelease',
        'AudioDramaRelease',
        'BackCoverImageRelease',
        'BookletBackImageRelease',
        'BookletFrontImageRelease',
        'BookletRelease',
        'Bundle',
        'ClassicalAlbum',
        'ClassicalDigitalBoxedSet',
        'ClassicalMultimediaAlbum',
        'ConcertVideo',
        'DigitalBoxSetRelease',
        'DjMix',
        'Documentary',
        'Drama',
        'DramaticoMusicalVideoRelease',
        'EBookRelease',
        'LongFormNonMusicalWorkVideoRelease',
        'LyricSheetRelease',
        'MultimediaAlbum',
        'MultimediaDigitalBoxedSet',
        'MultimediaSingle',
        'MusicalWorkBasedGameRelease',
        'NonMusicalWorkBasedGameRelease',
        'Playlist',
        'RingbackToneRelease',
        'RingtoneRelease',
        'Season',
        'Series',
        'SheetMusicRelease',
        'ShortFilm',
        'Single',
        'SingleResourceRelease',
        'StemBundle',
        'UserDefined',
        'VideoAlbum',
        'VideoMastertoneRelease',
        'VideoSingle',
        'WallPaperRelease'
        }
ReleaseRelationshipTypeSet = {
        'HasArtistFromEnsemble',
        'HasArtistFromSameEnsemble',
        'HasContentFrom',
        'HasEnsembleWithArtist',
        'HasSameArtist',
        'HasSameRecordingProject',
        'HasSimilarContent',
        'IsAudioUsedFor',
        'IsDifferentEncoding',
        'IsDigitalEquivalentToPhysical',
        'IsEquivalentToAudio',
        'IsEquivalentToVideo',
        'IsExtendedFromAlbum',
        'IsFromAudio',
        'IsFromVideo',
        'IsImmersiveEditionOf',
        'IsNonImmersiveEditionOf',
        'IsParentRelease',
        'IsPhysicalEquivalentToDigital',
        'IsReleaseFromRelease',
        'IsShortenedFromAlbum',
        'IsVideoUsedFor',
        'Unknown',
        'UserDefined'
        }
