from dataclasses import dataclass


@dataclass
class Pandra_settings:
    rpc: str
    contract: str
    api_key: str
    explorer_url: str
    name: str | None = None


@dataclass
class Destination_config:
    send_trough_contract: str
    method: str


routers = {
    'BNB': Pandra_settings(
        'https://rpc.ankr.com/bsc',
        '0x87a218Ae43C136B3148A45EA1A282517794002c8',
        'AHJKUWRP71R73DRJMZ2SKTKYNUAZQHNT8M',
        'api.bscscan.com',
        'BNB'
    ),

    'POLYGON': Pandra_settings(
        'https://polygon.llamarpc.com',
        '0x141A1fb33683C304DA7C3fe6fC6a49B5C0c2dC42',
        'HZXURVA1KRIKTDU3GZXR4EJY6BFPPWMZGM',
        'api.polygonscan.com',
        'POLYGON'
    ),

    'CORE': Pandra_settings(
        'https://rpc.coredao.org',
        '0x36e5121618c0Af89E81AcD33B6b8F5CF5cDD961a',
        '0e51e941ddd54a11a9e92ba7c53b81e8',
        'api.coresan.io',
        'CORE'
    ),

    'CELO': Pandra_settings(
        'https://rpc.ankr.com/celo',
        '0xb404e5233aB7E426213998C025f05EaBaBD41Da6',
        'RNHSFYDX8PAM5H9RDFDKW381QHN7W57W8E',
        'api.celoscan.io',
        'CELO'
    )
}

destinations = {
    "FROM_BNB": {

        "network": routers["BNB"],

        # POLYGON
        109: Destination_config(
            "0x3668c325501322ceb5a624e95b9e16a019cdebe8",
            "l0"
        ),
        # MANTLE
        181: Destination_config(
            "0x3668c325501322ceb5a624e95b9e16a019cdebe8",
            "l0"
        ),
        # COMBO
        114: Destination_config(
            "J",
            "zkbridge"
        ),
        # CELO
        125: Destination_config(
            "0x3668c325501322ceb5a624e95b9e16a019cdebe8",
            "l0"
        ),
        # opBNB
        116: Destination_config(
            "0xe09828f0da805523878be66ea2a70240d312001e",
            "zkbridge"
        ),
        # CoreDAO
        153: Destination_config(
            "0x3668c325501322ceb5a624e95b9e16a019cdebe8",
            "l0"
        )
    },
    "FROM_POLYGON": {
        "network": routers["POLYGON"],
        # opBNB
        116: Destination_config(
            "0x2e953a70c37e8cb4553dae1f5760128237c8820d",
            "zkbridge"
        ),
        # BNB
        102: Destination_config(
            "0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5",
            "l0"
        ),
        # MANTLE
        181: Destination_config(
            "0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5",
            "l0"
        ),
        # CELO
        125: Destination_config(
            "0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5",
            "l0"
        ),
        # CoreDAO
        153: Destination_config(
            "0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5",
            "l0"
        ),
        # COMBO
        114: Destination_config(
            "0x2e953a70c37e8cb4553dae1f5760128237c8820d",
            "zkbridge"
        )
    },
    "FROM_CELO": {
        "network": routers["CELO"],
        # BNB
        102: Destination_config(
            "0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6",
            "l0"
        ),
        # # MANTLE
        # 181: Destination_config(
        #     "0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6",
        #     "l0"
        # ),
        # POLYGON
        109: Destination_config(
            "0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6",
            "l0"
        ),
        # # CoreDAO
        # 153: Destination_config(
        #     "0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6",
        #     "l0"
        # ),
        # opBNB
        116: Destination_config(
            "0x24339b7f8d303527C8681382AbD4Ec299757aF63",
            "zkbridge"
        ),
        # COMBO
        114: Destination_config(
            "0x24339b7f8d303527C8681382AbD4Ec299757aF63",
            "zkbridge"
        )
    },
    "FROM_CORE": {
        "network": routers["CORE"],
        # BNB
        102: Destination_config(
            "0x3701c5897710F16F1f75c6EaE258bf11Ee189a5d",
            "l0"
        ),
        # POLYGON
        109: Destination_config(
            "0x3701c5897710F16F1f75c6EaE258bf11Ee189a5d",
            "l0"
        ),
        # opBNB
        116: Destination_config(
            "0x5c5979832a60c17bb06676fa906bedd1a013e18c",
            "zkbridge"
        ),
        # COMBO
        114: Destination_config(
            "0x5c5979832a60c17bb06676fa906bedd1a013e18c",
            "zkbridge"
        )
    }
}

abi = """[{"inputs":[{"internalType":"uint256","name":"_mintStartTime","type":"uint256"},{"internalType":"uint256","name":"_mintEndTime","type":"uint256"},{"internalType":"uint256","name":"_mintLimit","type":"uint256"},{"internalType":"string","name":"_metadataUri","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"InvalidQueryRange","type":"error"},{"inputs":[],"name":"MintERC2309QuantityExceedsLimit","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"OwnershipNotInitializedForExtraData","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"fromTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"toTokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"ConsecutiveTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"explicitOwnershipOf","outputs":[{"components":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"bool","name":"burned","type":"bool"},{"internalType":"uint24","name":"extraData","type":"uint24"}],"internalType":"struct IERC721A.TokenOwnership","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"explicitOwnershipsOf","outputs":[{"components":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"bool","name":"burned","type":"bool"},{"internalType":"uint24","name":"extraData","type":"uint24"}],"internalType":"struct IERC721A.TokenOwnership[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"userAddress","type":"address"}],"name":"getMintSurplus","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintEndTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintStartTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_newMetadataUri","type":"string"}],"name":"setMetadataUri","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_mintLimit","type":"uint256"}],"name":"setMintLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_mintStartTime","type":"uint256"},{"internalType":"uint256","name":"_mintEndTime","type":"uint256"}],"name":"setMintTimes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"tokensOfOwner","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"stop","type":"uint256"}],"name":"tokensOfOwnerIn","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]"""
l0_abi = """[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes","name":"_payload","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"_reason","type":"bytes"}],"name":"MessageFailed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"sourceToken","type":"address"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenID","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"sourceChain","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"sendChain","type":"uint16"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"ReceiveNFT","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes32","name":"_payloadHash","type":"bytes32"}],"name":"RetryMessageSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"_type","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_minDstGas","type":"uint256"}],"name":"SetMinDstGas","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_path","type":"bytes"}],"name":"SetTrustedRemote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"SetTrustedRemoteAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenID","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"recipientChain","type":"uint16"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"TransferNFT","type":"event"},{"inputs":[{"internalType":"bytes","name":"_encoded","type":"bytes"}],"name":"_parseTransfer","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint16","name":"tokenChain","type":"uint16"},{"internalType":"bytes32","name":"symbol","type":"bytes32"},{"internalType":"bytes32","name":"name","type":"bytes32"},{"internalType":"uint256","name":"tokenID","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint16","name":"toChain","type":"uint16"}],"internalType":"struct NFT721Bridge.Transfer721","name":"transfer","type":"tuple"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"chainFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"chainId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint16","name":"_recipientChain","type":"uint16"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateFee","outputs":[{"internalType":"uint256","name":"fee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"failedMessages","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"_configType","type":"uint256"}],"name":"getConfig","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"}],"name":"getTrustedRemoteAddress","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address","name":"_endpoint","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"isTrustedRemote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lzEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"nonblockingLzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"retryMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lzEndpoint","type":"address"}],"name":"setLzEndpoint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_path","type":"bytes"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"setTrustedRemoteAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_nativeChainId","type":"uint16"},{"internalType":"address","name":"_nativeContract","type":"address"},{"internalType":"address","name":"_wrapper","type":"address"}],"name":"setWrappedAsset","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint16","name":"_recipientChain","type":"uint16"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"transferNFT","outputs":[{"internalType":"uint64","name":"sequence","type":"uint64"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"trustedRemoteLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wrappedAssetData","outputs":[{"internalType":"uint16","name":"nativeChainId","type":"uint16"},{"internalType":"address","name":"nativeContract","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"address","name":"","type":"address"}],"name":"wrappedAssets","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]"""
zkbridge_abi = """[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldContract","type":"address"},{"indexed":true,"internalType":"address","name":"newContract","type":"address"}],"name":"ContractUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"pendingImplementation","type":"address"},{"indexed":true,"internalType":"address","name":"newImplementation","type":"address"}],"name":"NewPendingImplementation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"sourceToken","type":"address"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenID","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"sourceChain","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"sendChain","type":"uint16"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"ReceiveNFT","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"chainId","type":"uint16"},{"indexed":false,"internalType":"address","name":"nftBridge","type":"address"}],"name":"RegisterChain","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenID","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"recipientChain","type":"uint16"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"TransferNFT","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"MIN_LOCK_TIME","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId_","type":"uint16"}],"name":"bridgeContracts","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"chainId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"confirmContractUpgrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"destChainId","type":"uint16"}],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"impl","type":"address"}],"name":"isInitialized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"isWrappedAsset","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"chainId","type":"uint16"},{"internalType":"address","name":"contractAddress","type":"address"}],"name":"registerChain","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"destChainId","type":"uint16"},{"internalType":"uint256","name":"fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"lockTime","type":"uint256"}],"name":"setLockTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"zkBridge","type":"address"}],"name":"setZkBridge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"submitContractUpgrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"toUpdateTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"tokenID","type":"uint256"},{"internalType":"uint16","name":"recipientChain","type":"uint16"},{"internalType":"bytes32","name":"recipient","type":"bytes32"}],"name":"transferNFT","outputs":[{"internalType":"uint64","name":"sequence","type":"uint64"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"tokenChainId","type":"uint16"},{"internalType":"bytes32","name":"tokenAddress","type":"bytes32"}],"name":"wrappedAsset","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"zkBridge","outputs":[{"internalType":"contract IZKBridge","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"srcChainId","type":"uint16"},{"internalType":"address","name":"srcAddress","type":"address"},{"internalType":"uint64","name":"sequence","type":"uint64"},{"internalType":"bytes","name":"payload","type":"bytes"}],"name":"zkReceive","outputs":[],"stateMutability":"nonpayable","type":"function"}]"""
