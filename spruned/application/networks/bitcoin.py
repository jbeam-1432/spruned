from spruned.dependencies.pycoinnet.networks import MAINNET, TESTNET, REGTEST

mainnet = {
    'pycoin': MAINNET,
    'electrum_servers': 'bc_mainnet',
    'chain': 'main',
    'regex_legacy_addresses_prefix': '13',
    'electrum_concurrency': 4,
    'admitted_versions': [
        b'Satoshi:0.16.3'
    ],
    'tx0': '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b',
    'tx1': '0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098',
    'checkpoints': {
        0: "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
        1: "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048",
        11111: "0000000069e244f73d78e8fd29ba2fd2ed618bd6fa2ee92559f542fdb26e7c1d",
        33333: "000000002dd5588a74784eaa7ab0507a18ad16a236e7b1ce69f00d7ddfb5d0a6",
        74000: "0000000000573993a3c9e41ce34471c079dcf5f52a0e824a81e7f953b8661a20",
        105000: "00000000000291ce28027faea320c8d2b054b2e0fe44a773f3eefb151d6bdc97",
        134444: "00000000000005b12ffd4cd315cd34ffd4a594f430ac814c91184a0d42d2b0fe",
        168000: "000000000000099e61ea72015e79632f216fe6cb33d7899acb35b75c8303b763",
        193000: "000000000000059f452a5f7340de6682a977387c17010ff6e6c3bd83ca8b1317",
        210000: "000000000000048b95347e83192f69cf0366076336c639f9b7228e9ba171342e",
        216116: "00000000000001b4f4b433e81ee46494af945cf96014816a4e2370f11b23df4e",
        225430: "00000000000001c108384350f74090433e7fcf79a606b8e797f065b130575932",
        250000: "000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214",
        279000: "0000000000000001ae8c72a0b0c301f67e3afca10e819efa9041e458e9bd7e40",
        295000: "00000000000000004d9b4ef50f0f9d686fd69db2e03af35a100370c64632a983",
        478559: "00000000000000000019f112ec0a9982926f1258cdcc558dd7c3b7e5dc7fa148"
    },
    'rpc_port': 8332
}

testnet = {
    'pycoin': TESTNET,
    'chain': 'test',
    'electrum_servers': 'bc_testnet',
    'regex_legacy_addresses_prefix': 'nm',
    'electrum_concurrency': 1,
    'admitted_versions': [
        b'/Satoshi:0.16.3'
    ],
    'tx0': '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b',
    'tx1': 'f0315ffc38709d70ad5647e22048358dd3745f3ce3874223c80a7c92fab0c8ba',
    'checkpoints': {
        0: "000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943",
        1: "00000000b873e79784647a6c82962c70d228557d24a747ea4d1b8bbe878e1206",
        500000: "000000000001a7c0aaa2630fbb2c0e476aafffc60f82177375b2aaa22209f606",
        1000000: "0000000000478e259a3eda2fafbeeb0106626f946347955e99278fe6cc848414"
    },
    'rpc_port': 18332
}

regtest = {
    'pycoin': REGTEST
}
