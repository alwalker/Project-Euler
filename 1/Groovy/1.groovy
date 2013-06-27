def nums = (1..999).findAll({ it % 3 == 0 || it % 5 == 0 })
println nums.sum()
