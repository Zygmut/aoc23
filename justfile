set dotenv-load
set windows-shell := ["nu", "-c"]
year := "2023"

default:
  @just --list


[no-exit-message]
new day:
  @if (not ("{{day}}" | into int) in 1..31) { \
    echo "❌ Invalid day input. Please provide a numeric value between 1 and 31." ; exit 1 \
  }

  @mkdir ./day/{{day}}
  @cp ./day/template/* ./day/{{day}}/ --recursive

  @if (not "SESSION_COOKIE" in $env) { \
    "⚠️ SESSION_COOKIE not set" \
  } else { \
    echo "📥 Downloading input for day {{day}} ..." ; \
    http get -H {cookie: ($env.SESSION_COOKIE | prepend "session" | str join "=")} https://adventofcode.com/{{year}}/day/{{day}}/input | save -f ./day/{{day}}/data/input.txt \
  }

  @echo "✅ Successfully created day {{day}}. Happy coding!"


test day *args:
  @echo "🚧 WIP"


[no-exit-message]
run day *args:
  @echo "💡 Executing day {{day}} ..."
  @timeit {python ./day/{{day}}/main.py {{args}}}
