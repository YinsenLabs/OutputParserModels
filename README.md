# OutputParserModels

OutputParserModels is a Python module used to reuse and develop Pydantic models, to supplement the output structure information of LLMs during the result parsing process.

## Features

- Pre-defined Pydantic models for common LLM output structures
- Easy integration with existing LLM applications
- Type-safe output parsing
- Customizable model templates
- Support for various LLM frameworks

## Installation

```bash
pip install outputparsermodels
```

## Quick Start

```python
from predefined_model.llm_clients.gemini_calls import call_gemini_calendar_api
from predefined_model.models.calendar_api import CalendarAPIResponse

prompt = "Create a Google Calendar event for a team meeting on March 30, 2025, at 10 AM."

response :List[CalendarAPIResponse] = call_gemini_calendar_api(prompt)
```

## Project Structure

```
outputparsermodels/
├── predefined_model/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── calendar_event.py
│   │   └── free_busy.py
│   ├── llm_clients/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── gemini_calls.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_calendar_api.py
│   └── test_gemini_calls.py
├── examples/
│   └── calendar_example.py
├── README.md
├── requirements.txt
└── setup.py
```

## Usage

## Available Models

- `BaseOutputModel`: Base class for all output models
- `CalendarEventModel`: Response class for calendar event
- `CalendarFreeBusyModel`: Response class for free busy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Pydantic team for their excellent work
- Inspired by various LLM output parsing needs in production environments

## Contact

QuyThanh - tothanh1feb3.quinn@gmail.com

Project Link: [https://github.com/ToQuyThanh/PydanticParser](https://github.com/ToQuyThanh/PydanticParser)
