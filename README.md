# Transfer Limits Animation
## Introduction
A set of Python functions that animates flows between power system areas. The time-varying flows are supplied in a csv-formatted input file organized as follows.

DateTime | FromArea | ToArea | Value
---------|----------|--------|-------
20170611 0:00 | NYISO | NEISO | 1000
20170611 0:00 | IESO | NYISO | 500
20170611 0:00 | NYISO | PJM | -500
20170611 0:00 | NEISO | HQ | -1000
20170611 0:00 | HQ | NYISO | 500
20170611 1:00 | NYISO | NEISO | 800
... |
20170611 1:00 | HQ | NYISO | 400

This example system has 5 areas:
1. NYISO - New York Independent System Operator http://www.nyiso.com/
1. NEISO - New England Independent System Operator http://www.iso-ne.com/
1. PJM - Pennsylvania Jersey Maryland System Operator
http://www.pjm.com
1. HQ - Hydro Quebec http://www.hydroquebec.com/international/en/
1. IESO - Independent System Operator Ontario http://www.ieso.ca/

@jbebic1965 finish the Introduction    


# Practicing writing styles
It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)

# Practicing GitHub collaboration
Multiple contributors will create a sandwich recipe  
## SUBWAY sandwich
1. Choose bread
1. Select your meat
1. Select cheese:
  * Provolone
  * Swiss
  * Cheddar
1. Toasted?
  - [x] yes
1. Add veggies:
  * lettuce
  * tomatoes
  * spinach
  * black olives
  * peppers
1. Choose dressing:
  * mayo
  * chipottle
  * ranch
