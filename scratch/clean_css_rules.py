with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace block from .card-baroque-frame up to } before /* Very Small
old_block_1 = '''  .card-baroque-frame {
    inset: -6px -8px;
  }

  .card-floral-swag {
    width: 94%;
    max-height: 48px;
  }

  .card-floral-swag.swag-top {
    top: -42px;
  }

  .card-floral-swag.swag-bottom {
    bottom: -44px;
  }

  .card-parchment-body {
    min-height: auto;
    padding: 44px 18px 40px 18px;
  }

  .card-content-stack {
    gap: 4px;
  }

  .card-crown-ornament {
    width: 44px;
    margin-bottom: 0;
  }

  .celebrant-name {
    font-size: 3.3rem;
  }

  .emerald-roses-accent {
    max-width: 150px;
    margin: 2px auto;
  }

  .event-datetime-badge {
    width: 90%;
    max-width: 280px;
    margin: 3px 0;
  }
}'''

css = css.replace(old_block_1, '}')
css = css.replace(old_block_1.replace('\n', '\r\n'), '}')

# Replace in small mobile
old_block_2 = '''  .card-parchment-body {
    padding: 26px 12px 24px 12px;
  }

  .datetime-grid {
    padding: 6px 4px;
  }'''
css = css.replace(old_block_2, '')
css = css.replace(old_block_2.replace('\n', '\r\n'), '')

# Replace in landscape
css = css.replace('.royal-invitation-card {\n    margin: 20px 0;\n  }', '.royal-official-invitation-section {\n    margin: 20px 0;\n  }')
css = css.replace('.royal-invitation-card {\r\n    margin: 20px 0;\r\n  }', '.royal-official-invitation-section {\r\n    margin: 20px 0;\r\n  }')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Cleaned obsolete CSS rules!')
