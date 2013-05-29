#!/usr/bin/env ruby
require 'minitest/spec'
require 'minitest/autorun'
require_relative 'main'


describe 'Test Something' do

  it 'should fail' do
    assert_equal false, something
  end

  it 'should pass' do
    assert_equal true, something
  end

end
