//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "hardhat/console.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";


contract TellorColor is ERC721URIStorage {

    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("TellorColor", "TIC") {}


    function mint(address _recip, string memory _tokenURI) public returns (uint256) {

        // increment count of minted items
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(_recip, newItemId);
        _setTokenURI(newItemId, _tokenURI);

        return newItemId;
    }
}
