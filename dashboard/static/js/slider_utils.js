export function initializeSlider(slider, minYear, maxYear) {
	// const slider = $('#year-slider')[0];
	if (slider && slider.noUiSlider) {
		slider.noUiSlider.destroy();
	}
	noUiSlider.create(slider, {
		start: minYear,
		step: 1,
		range: {
			'min': minYear,
			'max': maxYear
		},
		tooltips: {
			to: function (value) {
				return value.toFixed(0);
			},
			from: function (value) {
				return Number(value);
			}
		},
		pips: {
			mode: 'values',
			values: [minYear, maxYear],
			density: 10
		}
	});
}

export function updateSlider(slider, minYear, maxYear) {
	const range = slider.noUiSlider.options.range;
	const newMinYear = Math.min(range.min, minYear)
	const newMaxYear = Math.max(range.max, maxYear)
	slider.noUiSlider.updateOptions({
		range: {
			'min': newMinYear,
			'max': newMaxYear
		}
	});
}
