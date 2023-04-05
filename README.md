# RSA


## Usage 
```
usage: RSA algorithm [-h] [-a {generate,encrypt,decrypt}] [-k KEY] [-i INPUT]
                     [-o OUTPUT]

Generates public/private keys + encodes/decodes text

optional arguments:
  -h, --help            show this help message and exit
  -a {generate,encrypt,decrypt}, --action {generate,encrypt,decrypt}
                        Choose type of action
  -k KEY, --key KEY     key for encoding/decoding
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file
```
## Examples 

Generating keys
```
python3 main.py -a generate 
public key: 420054129998730599,439527753393865333
private key: 65385685668271959,439527753393865333
```

Encrypting
```
python3 main.py -a encrypt -k 420054129998730599,439527753393865333 -i example_input -o example_output
```

Decrypting
```
python3 main.py -a decrypt -k 65385685668271959,439527753393865333 -i example_output -o example_output_decrypt
```
