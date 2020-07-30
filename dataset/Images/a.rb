# frozen_string_literal: false

user_input = 'Sample20_0.json'
puts user_input.to_s
user_input.chomp!("\n")

require 'json'
file = File.open user_input
data = JSON.load file
data['fields'].each_with_index do |field, _i|
  puts field['field_name']

  index = 0
  loop do
    puts "Enter: #{index}"
    input = gets
    input.chomp!("\n")
    break if input == 'asdf'

    data['textbox'].each_with_index do |text_box, _j|
      if text_box['text'].downcase.include? input.downcase
        puts "ID: #{_j} Text: #{text_box['text']}, Box: #{text_box['bbox']}, "
      end
    end
    puts 'Select ID:'
    id = gets
    id.chomp!("\n")
    id = id.to_i
    break if id == -1

    data['fields'][_i]['value_text'] << data['textbox'][id]['text']
    data['fields'][_i]['value_id'] << data['textbox'][id]['id']
    index += 1
    puts data['fields'][_i]
    puts 'IS THERE MORE?'
    more = gets
    break if more == "\n"
  end
end

File.open(user_input, 'w+') do |f|
  f.write(data.to_json)
end
