"""
All the exceptions that can be used in this module are placed here.
"""

from config import ReleaseTypeSet, ReleaseRelationshipTypeSet

class InvalidReleaseType(Exception):
    """
    Raises an Error if the given release_type does not belong
    to ReleaseTypeSet.
    """
    def __init__(self, release_type):
        self.release_type = release_type
        self.message = f"{self.release_type} does not belong to the ReleaseTypeSet. It must be from one of the following values\n{ReleaseTypeSet}"
        super().__init__(self.message)

class InvalidReleaseRelationshipTypeSet(Exception):
    """
    Raises an Error if the given relationship_type does not belong
    to ReleaseRelationshipTypeSet.
    """
    def __init__(self, relationship_type):
        self.relationship_type = relationship_type
        self.message = f"{self.relationship_type} does not belong to the ReleaseTypeSet. It must be from one of the following values\n{ReleaseRelationshipTypeSet}"
        super().__init__(self.message)

class NoNamespaceError(Exception):
    """
    Raises an Error if no Namespace argument has been given
    when it is required by the DDEX schema.
    """
    def __init__(self):
        self.message = f"No Namespace has been provided."
        super().__init__(self.message)
