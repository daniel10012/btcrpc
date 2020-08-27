import sys
from decimal import *
from extract import *
#https://intellipaat.com/community/4766/how-to-extract-all-used-hash160-addresses-from-bitcoin-blockchain
#to do
#manage case where type = pubkey (no address): https://bitcoin.stackexchange.com/questions/96865/why-does-vout-sometimes-not-have-address

from bitcoinrpc.authproxy import AuthServiceProxy

RPC_ADDRESS="127.0.0.1:8332"
RPC_USER="test"
RPC_PASSWORD="test"

def connect(address, user, password):
    return AuthServiceProxy("http://%s:%s@%s"%(user, password, address))

start_block = 200000
end_block = 200005

rpc = connect(RPC_ADDRESS, RPC_USER, RPC_PASSWORD)

outps = []
blocks = []


for i in range(start_block, end_block+1):
    block_hash = rpc.getblockhash(i)

    #Outputs
    outputs = extract_outputs(rpc, block_hash)
    outps.extend(outputs)

    #Blocks
    bl = extract_block(rpc, block_hash)
    blocks.append(bl.copy())



print(blocks)
print(outps)


