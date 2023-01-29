from lxml import etree as et
from enum import Enum
from utils import add_subelement_with_text, save
class Tags(Enum):
    deal_list = "DealList"
    release_deal = "ReleaseDeal"
    deal_release_reference = "DealReleaseReference"
    deal = "Deal"
    deal_terms = "DealTerms"
    validity_period = "ValidityPeriod"
    start_date = "StartDate"


class DealList:
    def __init__(
            self,
            reference,
            start_date,
            ):
        self.reference = reference
        self.start_date = start_date

    def build_validity_period(self):
        tag = et.Element(Tags.validity_period.value)
        add_subelement_with_text(tag, Tags.start_date.value, self.start_date)
        return tag

    def build_deal(self):
        tag = et.Element(Tags.deal.value)
        deal_terms = et.Element(Tags.deal_terms.value)
        deal_terms.append(self.build_validity_period())
        tag.append(deal_terms)
        return tag

    def build_release_deal(self):
        tag = et.Element(Tags.release_deal.value)
        add_subelement_with_text(
                tag, 
                Tags.deal_release_reference.value,
                self.reference
                )
        tag.append(self.build_deal())
        return tag

    def write(self):
        tag = et.Element(Tags.deal_list.value)
        tag.append(self.build_release_deal())
        return tag


if __name__ == "__main__":
    deal_list = DealList(
            reference="R1",
            start_date="2022-01-06"
            )
    root = deal_list.write()
    save(root, 'deal_list.xml')

