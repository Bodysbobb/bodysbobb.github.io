module Jekyll
  module HideCustomBibtex
    def hideCustomBibtex(input)
      keywords = @context.registers[:site].config['filtered_bibtex_keywords']

      keywords.each do |keyword|
        input = input.gsub(/^.*\b#{keyword}\b *= *\{.*$\n/, '')
        # Add this line to catch boolean values without curly braces
        input = input.gsub(/^.*\b#{keyword}\b *= *(true|false).*$\n/, '')
      end

      # Clean superscripts in author lists
      input = input.gsub(/^.*\bauthor\b *= *\{.*$\n/) { |line| line.gsub(/[*†‡§¶‖&^]/, '') }

      # Fix any dangling commas
      input = input.gsub(/,(\s*\})/, '\1')
      
      return input
    end
  end
end

Liquid::Template.register_filter(Jekyll::HideCustomBibtex)