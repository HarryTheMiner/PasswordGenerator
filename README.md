 🔐 Random Password Generator<br>
A simple Python script that generates secure, random passwords using a mix of uppercase letters, lowercase letters, numbers, and special characters.<br>

📌 Features<br>
-Generates strong passwords.<br>
-User-defined password length.<br>
-Uses randomness for security.<br>

🛠 Key Methods Used<br>
1️⃣ string.ascii_*<br>
The string module provides predefined sequences of characters:<br>

ascii_uppercase → Contains uppercase letters (A-Z).<br>

ascii_lowercase → Contains lowercase letters (a-z).<br>

digits → Contains numbers (0-9).<br>

punctuation → Contains special characters (!@#$%^&*, etc.).<br>
These help in creating a diverse set of characters for password generation.<br>

2️⃣ .extend()<br>
The extend() method is used to add multiple elements from an iterable (like a list or string) to an existing list. Instead of adding a single element, it merges all characters from another list or sequence into the current list. This ensures all character types are included in the password.
<br>
3️⃣ random.shuffle()<br>
This function randomizes the order of elements in a list in place. It ensures that the generated password does not follow any predictable pattern, making it more secure against attacks.
<br>
4️⃣ "".join()<br>
The join() method is used to convert a list of characters into a single string. After shuffling, the password is formed by combining a specific number of characters into a final output string.
<br>
🔒 Note<br>
This script generates passwords but does not store them. Use a password manager for secure storage.<br>
