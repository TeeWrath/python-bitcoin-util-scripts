from bitcoinutils.setup import setup
from bitcoinutils.keys import P2shAddress, PrivateKey
from bitcoinutils.script import Script

def main():
    setup('testnet')
    
    p2pk_sk = PrivateKey('cRvyLwCPLU88jsyj94L7iJjQX5C2f8koG4G2gevN4BeSGcEvfKe9')
    
    p2pk_pk = p2pk_sk.get_public_key()
    
    p2pk_addr = p2pk_pk.get_address()
    
    redeem_script = Script([p2pk_pk.to_hex(), 'OP_CHECKSIG'])
    
    addr = P2shAddress.from_script(redeem_script)
    
    print(f'Printed stuff is: {addr.to_string()}')
    
if __name__ == "__main__":
    main()