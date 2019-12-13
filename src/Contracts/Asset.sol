pragma solidity ^0.4.24;

import "./Table.sol";

contract Asset {
    string[] accountList;
    mapping(string=>address) name_to_addr;
    mapping(address=>string) addr_to_name;

    event PayEvent(int256 ret);
    event RegisterEvent(int256 ret, string account, uint256 value);
    event TransferEvent(int256 ret, string from_account, string to_account, uint256 amount);
    
    constructor() public {
        createTable();
    }

    function createTable() private {
        TableFactory tablefactory = TableFactory(0x1001);
        tablefactory.createTable("asset", "account", "value");
    }

    function openTable() private view returns(Table) {
        TableFactory tablefactory = TableFactory(0x1001);
        Table table = tablefactory.openTable("asset");
        return table;
    }

    //账户登录
    function login(address addr) public view returns(int){
        if (name_to_addr[addr_to_name[addr]] != address(0)){
            return 1;//代表企业已注册
        }
        return 0;//代表企业未注册
    }

    //资产注册
    function register(address addr, string memory account, uint256 value) public returns(int256){
        int256 infocode = 0;
        int256 ret = 0;
        uint256 temp = 0;
        // 查询账户是否存在
        (ret, temp) = select(account);
        if(ret == 0) {
            infocode = -1;//账户已存在
        } else {//账户不存在
            name_to_addr[account] = addr;
            addr_to_name[addr] = account;
            accountList.push(account);
            Table table = openTable();
            Entry entry = table.newEntry();
            entry.set("account", account);
            entry.set("value", int256(0));
            int count = table.insert(account, entry);
            if (count == 1) {
                infocode = 0;//注册成功
            } else {
                infocode = -2;//其他错误
            }
        }

        emit RegisterEvent(infocode, account, value);

        return infocode;
    }

    //支付账单
    function pay() public returns(int256){
        Table table = openTable();
        for(uint i = 0; i < accountList.length; i++){
            Entry entry = table.newEntry();
            entry.set("account", accountList[i]);
            entry.set("value", int256(0));
            table.update(accountList[i], entry, table.newCondition());
        }
        emit PayEvent(0);
        return 0;
    }

    //资产查询
    function select(string memory account) public view returns(int256) {
        Table table = openTable();
        Entries entries = table.select(account, table.newCondition());
        if (0 == uint256(entries.size())) {
            return -1;//账户不存在，返回-1
        } else {
            Entry entry = entries.get(0);
            return uint256(entry.getInt("value"));//账户存在，返回资产金额
        }
    }

    //账户间转移资产
    function transfer(address addr, string memory to_account, uint256 amount) public returns(int256) {
        string memory from_account = addr_to_name[addr];
        int infocode = 0;
        int256 ret = 0;
        uint256 from_value = 0;
        uint256 to_value = 0;
        
        (ret, from_value) = select(from_account);
        if(ret != 0) {// 转移账户不存在
            infocode = -1;
            emit TransferEvent(infocode, from_account, to_account, amount);
            return infocode;

        }

        (ret, to_value) = select(to_account);
        if(ret != 0) {//接收账户不存在
            infocode = -2;
            emit TransferEvent(infocode, from_account, to_account, amount);
            return infocode;
        }

        if(from_value < amount) {// 转移资产的账户金额不足
            infocode = -3;
            emit TransferEvent(infocode, from_account, to_account, amount);
            return infocode;
        }

        Table table = openTable();
        Entry entry0 = table.newEntry();
        entry0.set("account", from_account);
        entry0.set("value", int256(from_value - amount));
        int count = table.update(from_account, entry0, table.newCondition());
        if(count != 1) {
            infocode = -4;//其他错误
            emit TransferEvent(infocode, from_account, to_account, amount);
            return infocode;
        }
        Entry entry1 = table.newEntry();
        entry1.set("account", to_account);
        entry1.set("value", int256(to_value + amount));
        table.update(to_account, entry1, table.newCondition());
        emit TransferEvent(infocode, from_account, to_account, amount);

        return infocode;
    }

}