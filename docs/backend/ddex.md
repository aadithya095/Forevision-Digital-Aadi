# DDEX Module Documentation
The ddex module is divided into seperate modules in itself. Each module 
represents the major components that makes up the ddex xml. The major 
components of ddex are given below:

+ NewReleaseMessage
    + MessageHeader
    + PartyList
    + ReleaseList
    + ResourceList
    + DealList

The overall structure of the module is given under:
+ ddex
    + builder
    + messageheader
    + party
    + utils

## builder module
The builder module comprises of Builder object (class) that helps to build and 
save the ddex xml file. To create a builder just import the class and provide 
the sender and receiver arguments. The sender and receiver arguments are of 
Sender and Receiver type.

```
from ddex.builder import Builder
builder = Builder(sender=sender, receiver=receiver)
output_file = 'test.xml'
root = builder.create() # returns the root of the xml document ie 
NewReleaseMessage builder.save(root, output_file) # saves the xml file in the 
output location
```

## messageheader module
The messageheader module consists of MessageHeader object (class) that helps in 
creating MessageHeader component of the ddex file. The MessageHeader class 
accepts four arguments i.e. sender, receiver, thread id and message id. If 
thread id and message id are not provided it atomatically genereates one. It 
returns the MessageHeader tag of the xml as the root element

```
from ddex.messageheader import MessageHeader
messagebody = MessageHeader(sender=sender, receiver=receiver)
message_tag = messagebody.create()
```

## party module
The party module consists of Party object(class) that helps to create parties. 
The Party class accepts three optional argument and one compulsory argument 
reference_id, party_id, full_name, party_role. If the party_role is None then 
party_id value is not accepted and reference_id is accepted. If party_role is 
either Sender of Receiver then reference_id is not accepted party_id is 
accepted. fullname is compulsary for all.

It returns the Party tag as the root element.

```
from ddex.party import Party
party_role = "Sender"
party_id = 'partyid'
fullname = 'fullname'
party = Party(fullname, party_role=party_role, party_id=party_id)
sender = party.create()
```

## utils module
The utils module consists of utility functions that can be reused to do a 
specific task and can be used to test the xml created. It consists of the 
following utility functions.

### add_subelement_with_text
This function accepts the argument root, tagname, tagtext. It is used to insert 
a subelement tag with text in it. For example, say we have to create the 
follwing xml.
```
<Party>
    <PartyId>SomeId</PartyId>
</Party>
```
Here Party is the element tag and PartyId is the subelement of Party with some 
text "SomeId" to create such a subelement tag with text we use this function.

```
from ddex.utils import add_subelement_with_text
text = "SomeId"
tagname = "PartyId"
root = party

add_subelement_with_text(root, tagname, text)
```
### reparse_xml
This function is used for testing purposes only. It can parse the xml code 
formed by the element to a string.
```
from ddex.messageheader import MessageHeader
messagebody = MessageHeader(sender=sender, receiver=receiver)
message = messagebody.create()

xml = reparse_xml(message)
```
### prettyprint
This function is used tp print the reparsed_xml output to the console. Only to 
be used for testing purposes and during development.


# Testing the DDEX module
In order to test the DDEX module go to the `./src/tests/` directory and run the 
following command:
```
$ pytest -vv # for very verbose and detailed 
$ pytest # for normal output
```
