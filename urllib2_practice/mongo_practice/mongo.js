db.one.insert({
    _id:1,
    name:"张三",
    age:28
})

db.one.insert({
    name:"老王",
    age:28
})

dict = {
    _id:2,
    name:"小王",
    age:18
}
db.one.insert(dict)

//3.删除

db.xx.remove()

//1.删除老王
    db.one.remove({name:"老王"})
//删除所有的男生（默认 符合条件的都删除）
    db.one.remove({gender:false})
//3.只删除符合条件的第一个
    db.one.remove({gender:true},{justOne:true})
//4.全部删除
    db.one.remove({})

//4.修改 update
//1.修改小明的名字 根据id
    db.one.update({_id:4},{name:"大明"})
    db.one.update({_id:5},{like:"男朋友"})

//2.只想修改制定的字段，其他的不变$set
     db.one.update({_id:7},{$set:{like:"男朋友"}})

//3.默认符合条件的只修改一个；全部修改$multi
    //男生的年龄修改为30
    db.one.update(
        {gender:true},
        {$set:{age:30}}
        )
    //女生的年龄修改为12
    db.one.update(
        {gender:false},
        {$set:{age:12}},
        {multi:true}
        )
db.one.insert({_id:1,name:"老王",age:88,gender:false})
db.one.insert({_id:2,name:"小王",age:25,gender:false})
db.one.insert({_id:3,name:"小蓝",age:18,gender:false})
db.one.insert({_id:4,name:"小明",age:20,gender:true})
db.one.insert({_id:5,name:"小红",age:30,gender:false})
db.one.insert({_id:6,name:"小绿",age:40,gender:true})
db.one.insert({_id:7,name:"小花",age:50,gender:true})
db.one.insert({_id:8,name:"小美",age:60,gender:false})

//5.基本文档的查询
    //1.查询所有数据 db.xx.find()
        //格式化输出 db.xx.find().pretty()
    //2.查询所有女生数据
        db.stu.find({gender:false})
    //3.只返回符合条件的第一个
        db.stu.findOne({gender:false})

//6.查询条件运算： $lt $gt $lte $ne(不等于)
    //1.筛选年龄大于20岁的
    db.stu.find({age:{$gt:20}})
    //2.条件查询  $lt $gt $lte $ne(不等于)
    //3.逻辑运算：$and $or
    db.stu.find({age:16,gender:true})
    db.stu.find({$and:[{age:16}, {gender:true}]})
    // 年龄大于20：男生
    db.stu.find({$and:[{age:{$gt:20}}, {gender:true}]})
    //年龄大于20或者性别false 女生
    db.stu.find({$or:[{age:{$gt:20}}, {gender:true}]})
    //$and  和 $or 混用
        //年龄小于45岁或者是女生；必须是来自桃花岛
            db.stu.find({$and:[{$or:[{age:{$lt:45}},{gender:false}]},{hometown:"桃花岛"}]})
        // 来自蒙古或者是大理的人 要求必须是男士
            db.stu.find({$and:[{$or:[{hometown:"蒙古"}, {hometown:"大理"}]}, {gender:true}]})

    // 范围运算： $in $nin   db.xx.find({字段: {运算符:[值]}})
            // 取18,20,40岁的人
                db.stu.find({age:{$in:[18,20,40]}})
            // 来自蒙古或者是大理的人
                db.stu.find({hometown:{$in:['蒙古', '大理']}})

    // 正则表达式
        db.stu.insert({ "_id" : 7, "name" : "liu", "hometown" : "大理", "age" : 55, "gender" : true })
            // db.xx.find({字段：/正则/})
            // db.xx.find({字段：{$regex:"正则"}})

            // 姓段 db.xx.find({字段：/正则/})
                db.stu.find({name:/段/})

            // 忽略大小写
                db.stu.find({name:{$regex:"liu", $options:"i"}})
                db.stu.find({name:/liu/i})

    // 自定义函数   db.xx.find({$where:带返回值的匿名函数})
        //年龄小于18的人
            db.stu.find({$where:function () {return this.age < 18}})

// 数据查询结果显示
    db.stu.find().limit(3)
    db.stu.find().limit(3).skip(2)
    db.stu.find().skip(2).limit(3)
