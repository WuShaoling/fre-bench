# 安装依赖
# gem install rspec i18n mime-types aws-sdk-core minitest thread_safe addressable diff-lcs bundler multi_json

packages = [
    "rspec",
    "mime-types",
    "i18n",
    "aws-sdk-core",
    "minitest",
    "thread_safe",
    "addressable",
    "diff-lcs",
    "bundler",
    "multi_json"
]

# 预先加载
packages.each { | item |
    t1 = Time.now.strftime('%Y%m%d%H%M%S%L')
    require item
    t2 = Time.now.strftime('%Y%m%d%H%M%S%L')
     puts(item + " : " + String(Integer(t2) - Integer(t1)))
}

# 子进程中加载
packages.each { | item |
    t1 = Time.now.strftime('%Y%m%d%H%M%S%L')
    pid = Process.fork do
        require item
        t2 = Time.now.strftime('%Y%m%d%H%M%S%L')
        puts(item + " : " + String(Integer(t2) - Integer(t1)))
    end
    Process.wait
}

=begin
rspec : 89
mime-types : 166
i18n : 57
aws-sdk-core : 550
minitest : 31
thread_safe : 22
addressable : 118
diff-lcs : 29
bundler : 80
multi_json : 18

rspec : 2
mime-types : 3
i18n : 2
aws-sdk-core : 3
minitest : 3
thread_safe : 3
addressable : 4
diff-lcs : 2
bundler : 4
multi_json : 3
=end