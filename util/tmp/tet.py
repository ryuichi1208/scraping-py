ass ClassSample
  @instance_var = "hoge"
  @@class_var = "moge"

  def self.class_method
    puts "#{self}, instance_var: #{@instance_var}, class_var: #{@@class_var}"
  end
end

class SubclassSample < ClassSample
  @instance_var = "foo"
  @@class_var = "bar"
end

ClassSample.class_method # -> ClassSample, instance_var: hoge, class_var: bar
SubclassSample.class_method # -> SubclassSample, instance_var: foo, class_var: bar
