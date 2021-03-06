from decimal import *


# Outputs
def extract_outputs(rpc, block_hash):

    block = rpc.getblock(block_hash)
    output = {}
    outputs = []
    for tx in block[u'tx']:
        raw_tx = rpc.getrawtransaction(tx, True)

        for vout in raw_tx["vout"]:
            output["index"] = vout["n"]
            output["txid"] = raw_tx["txid"]
            output["value"] = Decimal(vout["value"])
            output["type"] = vout["scriptPubKey"]["type"]

            outputs.append(output.copy())

    return outputs

# Blocks
def extract_block(rpc, block_hash):

    block = rpc.getblock(block_hash)

    bl = {}
    bl["hash"] = block_hash
    bl["height"] = block["height"]
    bl["time"] = block["time"]
    bl["prevhash"] = block["previousblockhash"]

    return bl

# Transactions

def extract_transactions(rpc, block_hash):

    block = rpc.getblock(block_hash)

    t = {}
    txs = []
    for tx in block[u'tx']:
        raw_tx = rpc.getrawtransaction(tx, True)
        t["txid"] = raw_tx["txid"]
        txs.append(t.copy())

    return txs

# Addresses

def extract_addresses(rpc, block_hash):

    block = rpc.getblock(block_hash)
    addresses = []

    for tx in block[u'tx']:
        raw_tx = rpc.getrawtransaction(tx, True)

        if not 'vout' in raw_tx:
            break

        for vout in raw_tx[u'vout']:

            if not "scriptPubKey" in vout:
                break

            if vout["scriptPubKey"]["type"] == "nulldata":
                # arbitrary data
                break

            elif 'addresses' in vout['scriptPubKey']:
                addresses.extend(vout['scriptPubKey']['addresses'])

            else:
                break

    return addresses




