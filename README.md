# Let's Script
A tech talk in code I wish I had heard as a n00b. In this talk, we'll look at code and see how simple strategies like making methods in your scripts sets you up for success as your needs change.

## Prologue
Let's start by talking about when to script. Script a solution when:
* scripting is just as labor intensive (or maybe just a bit more -- learning investment!) as doing it by hand.
* if you are concerned about accuracy.
* if you will need to do this process again in the future.


## The Problem
Before we begin, let's talk about the problem we are trying to solve in code. A college campus has two systems that don't talk to each other: a mail system and a VPN system. Everyone on campus has a unique email username, but not everyone has a VPN account. If you request a VPN account, one will be created using your email username and a 'vpn-' prefix as your username. We know which graduates need to have their email addresses expired, but we aren't sure which ones need to have their vpn account expired as well.

Given a list of graduate userids and all VPN accounts, determine which vpn accounts need to be expired.

Other classes of students may need to be accounted for in the future like:
* deans leave - email and VPN access for up to three years of leave (gap year etc)
* college leave - email and VPN revoked after incident (having a still in your dorm room)

# Set Up, To Play Along at Home
## Install Requirements

```
#make the virtual env
virtualenv env

# install required packages
pip install -r requirements.txt
```

## Generate Example Files (optional)
Tune constants as needed.

```
python make_user_lists.py
```

## Run Tests

```
py.test
```

## Easy Peasy Execution of Examples
Tune execution as needed.

```
./run.sh
```

# Take Aways by Script
## vpn_expire_list_v1
* simple solution to the problem, but repetitive, no unit tests, not so configurable

## vpn_expire_list_v1_refined
* DRYer solution to the problem, more configurable, no unit tests

## vpn_expire_list_v1_tested
* broken into testable parts

## vpn_expire_list_v2
* rules of the game change, the script has to grow with it.
* using sys args (positional args) to configure. Works but is clumsy and error prone.
* still getting the advantage of tests b/d builds on DRY code and tests

## vpn_expire_list_refined
* uses parser, so I can add args in any order from the commandline
* gives helpful hints and defaults, should I need them
* still not so flexible, what if a file is missing

## vpn_expire_list_v2_with_configs
* easier to manage
* handy, since I how have more stuff to think about like the deans leave list and departure year
* configs can now be updated and maintained in source control
* testable
* still not so great, what if I don't get college leave or deans leave students

## vpn_expire_list_v2_with_configs_sophisticated
* all the benefits of something with a config file
* will add in student and perform calculations based on presence in config.





