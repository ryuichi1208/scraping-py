class ClassSample:
  class_var = "hoge"

  @classmethod
  def class_method(cls):
    print "%s, class_var: %s" % (cls, cls.class_var)

  @staticmethod
  def static_method():
    print "%s, class_var: %s" % (ClassSample, ClassSample.class_var)

class SubclassSample(ClassSample):
  class_var = "foo"

ClassSample.class_method() # -> __main__.ClassSample, class_var: hoge
ClassSample.static_method() # -> __main__.ClassSample, class_var: hoge
SubclassSample.class_method() # -> __main__.SubclassSample, class_var: foo
SubclassSample.static_method() # -> __main__.ClassSample, class_var: hoge
