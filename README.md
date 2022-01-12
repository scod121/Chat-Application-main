## Chat Application

Developed a Chat application for messaging in-place using tKinter GUI toolkit in python.

Description : 

	- Users are identified by unique user id (String).
	- Groups, which are sets of users who are members of the group, are identified
	by a unique group id.
	- Contacts list of other users who are contacts of a given user.
	- Users can post messages in the form of a string and / or an image.

Like in a social network, posts of users can be to a contact or a group. All posts to a group appear in the incoming messages list for all members of the group. All direct posts from a contact also appear as incoming messages.

Since it is a extremely scaled down version of real Chat applications, all messages are stored in a file names messages.txt.
This is to be operated on same system, (in-place chat application).

![WhatsApp Image 2021-07-14 at 14 57 46 (1)](https://user-images.githubusercontent.com/53087905/125599587-6a2005e3-8576-4845-bfbd-2d920ab61308.jpeg)

![WhatsApp Image 2021-07-14 at 14 57 46](https://user-images.githubusercontent.com/53087905/125599621-f6883e81-7a55-433a-870b-368373a234df.jpeg)

![WhatsApp Image 2021-07-14 at 14 57 46 (2)](https://user-images.githubusercontent.com/53087905/125599631-a2d352f7-2972-4d2b-8d77-dd5f9a50f2b9.jpeg)


Format of social_network.txt : 

# users
<user_id1: contact_user1, contact_user2, …>
…
<user_idn: contact_user1, contact_user2, …>
#groups
<group_id1: member1, member2, …>
…
<group_idn: member1, member2, …>

Additionally, all the posted messages are saved in file messages.txt, for future runs of the program.
There are four visual modules to be displayed on the screen. Each module displays information pertaining to a current user. The information in the modules can change dynamically as the user changes. The modules are:
- A module to display incoming messages. The text of the message and the image (if any) displayed, formatted appropriately.
- A module to display existing contacts.
- A module to display groups of which the current user is member of.
- A module to compose and post messages.
Additionally, there is a droplist / menu for selecting the current user.

Divyansh Bhatia
