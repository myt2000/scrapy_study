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


//1.聚合查询：管道  db.xx.aggregate([{管道1}, {管道2}, {管道3}])
    // $group: db.xx.aggregated([{$group:}])
        // 将数据 按照 性别分组
            db.stu.aggregate([{$group:{_id:"$gender"}}])
        // 按照性别分组，求出每组年龄的平均值   $avg $sum $max $min $last $first $push
            db.stu.aggregate({$group:{_id:"$gender", age_avg:{$avg:"$age"}}})
        // 按籍贯分组 求每个地方的年龄之和
             db.stu.aggregate({$group:{_id:"$hometown",age_sum:{$sum:"$age"}}})

        // push 将获取的字段 按照分组 显示
        // 按照性别分组， 求出 每组的籍贯有哪些
            db.stu.aggregate({$group:{_id:"$gender", address:{$push:"$hometown"}}})

    // $match
        // 求出 年龄大于18岁的人
        db.stu.find({age:{$gt:18}})
        db.stu.aggregate({$mathc:{age:{$gt:18}}})
        // 求出 年龄小于40岁：按照性别分组
            db.stu.aggregate({$match:{age:{$lt:40}}}, {$group:{_id:"$gender", name_list:{$push:"$name"}}})

    // $project 投影：允许查看某个字段 db.xx.aggregate({$project:{字段;1, 字段:0}})

    // $sort
    // $limit
    // $skip
    // $unwind

// 2.索引操作 ：通过索引查询 效率最高 时间
        for (index = 0 ; index<200000; index++) {
            db.stu.insert(
                {
                    _id:index,
                    name:"name"+index,
                    age:index
                }
            )
        }
        db.stu.find({name:"name199999"}).explain("executionStats")
        //  通过id查询
        db.stu.find({id:"199999"}).explain("executionStats")