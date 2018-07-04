"python代码处， 缩进要注意
python <<EOF
import vim
def replace():
  source=vim.eval("a:source") #获取参数 source
  dest=vim.eval("a:dest") #获取参数 dest

  cmd="%s/{0}/{1}/".format(source,dest)
  #print(cmd) #直接输出到命令区
  vim.command(cmd)

EOF

"此处定义vim函数，内部来调用python方法
function! Replace(source,dest)
"a:source 才是source参数的正确访问方式，和其它语言不一样
"echo a:source

"无法直接传递vim参数给python
"估计可以通过参数封装函数来进行中转
"有待改进
  python replace()

endfunction
