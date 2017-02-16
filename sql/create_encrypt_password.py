import hashlib
import uuid
algorithm = 'sha512'     # name of the algorithm to use for encryption
passwords = ['paulpass93','rebeccapass15','bob1pass']    # unencrypted password
for password in passwords:
    salt = uuid.uuid4().hex  # salt as a hex string for storage in db
    m = hashlib.new(algorithm)
    m.update(str(salt + password).encode('utf-8'))
    password_hash = m.hexdigest()
    print (password+":"+"$".join([algorithm,salt,password_hash]))