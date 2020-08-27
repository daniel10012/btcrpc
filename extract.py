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

    bl ={}
    block = rpc.getblock(block_hash)
    bl["hash"] = block_hash
    bl["height"] = block["height"]
    bl["time"] = block["time"]
    bl["prevhash"] = block["previousblockhash"]

    return bl


