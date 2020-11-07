#!/usr/bin/env ruby
puts ARGV[0].scan(/[mos]:([-:+a-zA-Z0-9]+)/).join(",")
